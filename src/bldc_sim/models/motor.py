"""MotorParams and the lumped performance model tying winding + magnetics together.

Conventions:
- One coil per phase (3-slot concentrated winding), star or delta.
- BEMF treated as sinusoidal: peak phase EMF e = N * Phi * omega_e.
- Torque-speed uses the DC-equivalent line: T = Kt * (V - Ke_ll * w) / R_drive,
  clipped at the current limit.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, asdict

import numpy as np

from .magnetic import MagneticResult, solve_magnetics
from .winding import WindingResult, solve_winding

RPM_TO_RAD_S = 2 * math.pi / 60


@dataclass
class MotorParams:
    # Topology
    n_slots: int = 3
    n_poles: int = 4
    connection: str = "star"  # "star" | "delta"
    # Geometry (mm)
    stator_tip_r: float = 21.0
    air_gap: float = 1.5
    mag_t: float = 2.75
    mag_w: float = 9.25
    mag_l: float = 28.82
    tooth_stem_w: float = 8.0
    tooth_h: float = 10.0
    tip_thick: float = 1.0
    stack_len: float = 31.0
    rotor_wall: float = 3.0
    # Magnets
    br: float = 1.2
    k_air: float = 0.05
    calibration: float = 1.0
    # Winding
    turns_per_tooth: int = 40
    awg: int = 24
    packing: float = 0.55
    # Drive / test conditions
    v_bus: float = 11.1
    i_max: float = 10.0
    hand_spin_rpm: float = 300.0
    esc_bemf_threshold_v: float = 0.5
    rpm_max: float = 6000.0

    @property
    def mag_face_r(self) -> float:
        return self.stator_tip_r + self.air_gap

    @property
    def rotor_od(self) -> float:
        return 2 * (self.mag_face_r + self.mag_t + self.rotor_wall)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class Performance:
    magnetic: MagneticResult
    winding: WindingResult
    ke_phase: float  # peak phase V per mech rad/s
    ke_ll: float  # peak line-line V per mech rad/s
    kt: float  # N*m per peak phase A
    kv_rpm_per_v: float
    no_load_rpm: float
    stall_torque: float
    stall_current: float
    r_drive: float  # resistance the ESC drives through (two phases on)
    bemf_ll_at_hand_spin: float
    esc_verdict: str  # "pass" | "marginal" | "fail"


def solve(p: MotorParams) -> Performance:
    mag = solve_magnetics(
        br_t=p.br,
        mag_t_mm=p.mag_t,
        air_gap_mm=p.air_gap,
        mag_w_mm=p.mag_w,
        mag_l_mm=p.mag_l,
        k_air=p.k_air,
        calibration=p.calibration,
    )
    wind = solve_winding(
        turns_per_tooth=p.turns_per_tooth,
        awg=p.awg,
        packing=p.packing,
        n_slots=p.n_slots,
        stator_tip_r_mm=p.stator_tip_r,
        tip_thick_mm=p.tip_thick,
        tooth_stem_w_mm=p.tooth_stem_w,
        tooth_h_mm=p.tooth_h,
        stack_len_mm=p.stack_len,
        connection=p.connection,
    )

    pole_pairs = p.n_poles / 2
    ke_phase = p.turns_per_tooth * mag.flux_per_pole_wb * pole_pairs
    if p.connection == "star":
        ke_ll = math.sqrt(3) * ke_phase
        r_drive = 2 * wind.r_phase_ohm
    else:
        ke_ll = ke_phase
        r_drive = 2 / 3 * wind.r_phase_ohm

    # Sinusoidal 3-phase: T = (3/2) * ke_phase(peak) * I_phase(peak)
    kt = 1.5 * ke_phase

    no_load_w = p.v_bus / ke_ll if ke_ll > 0 else float("inf")
    no_load_rpm = no_load_w / RPM_TO_RAD_S
    kv = no_load_rpm / p.v_bus if p.v_bus > 0 else float("inf")

    stall_current = min(p.v_bus / r_drive, p.i_max)
    stall_torque = kt * stall_current

    bemf_hand = ke_ll * p.hand_spin_rpm * RPM_TO_RAD_S
    if bemf_hand >= p.esc_bemf_threshold_v:
        verdict = "pass"
    elif bemf_hand >= 0.5 * p.esc_bemf_threshold_v:
        verdict = "marginal"
    else:
        verdict = "fail"

    return Performance(
        magnetic=mag,
        winding=wind,
        ke_phase=ke_phase,
        ke_ll=ke_ll,
        kt=kt,
        kv_rpm_per_v=kv,
        no_load_rpm=no_load_rpm,
        stall_torque=stall_torque,
        stall_current=stall_current,
        r_drive=r_drive,
        bemf_ll_at_hand_spin=bemf_hand,
        esc_verdict=verdict,
    )


def bemf_curve(p: MotorParams, perf: Performance, n_points: int = 200):
    """RPM sweep -> (rpm, peak phase BEMF, peak line-line BEMF)."""
    rpm = np.linspace(0, p.rpm_max, n_points)
    w = rpm * RPM_TO_RAD_S
    return rpm, perf.ke_phase * w, perf.ke_ll * w


def torque_speed_curve(p: MotorParams, perf: Performance, n_points: int = 200):
    """RPM sweep -> (rpm, torque N*m, current A) under V and I limits."""
    rpm = np.linspace(0, max(perf.no_load_rpm, 1.0), n_points)
    w = rpm * RPM_TO_RAD_S
    i = np.clip((p.v_bus - perf.ke_ll * w) / perf.r_drive, 0, p.i_max)
    torque = perf.kt * i
    return rpm, torque, i


def copper_loss_curve(p: MotorParams, perf: Performance, n_points: int = 200):
    """Current sweep -> (I, copper loss W, torque N*m) with two phases conducting."""
    i = np.linspace(0, p.i_max, n_points)
    p_cu = i**2 * perf.r_drive
    torque = perf.kt * i
    return i, p_cu, torque
