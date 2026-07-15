"""Air-gap flux estimate for an air-core (plastic stator) BLDC.

With an iron stator and iron rotor back, the classic surface-magnet estimate is
B_gap ~ Br * t_m / (t_m + g). A plastic machine has no low-reluctance return
path, so the real field at the coil is far lower and spreads widely. We keep
the load-line form and multiply by an explicit air-core derating factor k_air
(default 0.05: no stator iron AND no rotor back-iron, so only a small fraction
of the magnet flux actually links the coil) plus a calibration scale the user
can anchor to a bench BEMF measurement.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MagneticResult:
    b_gap_t: float  # effective flux density at the coil, tesla
    pole_area_mm2: float
    flux_per_pole_wb: float


def solve_magnetics(
    *,
    br_t: float,
    mag_t_mm: float,
    air_gap_mm: float,
    mag_w_mm: float,
    mag_l_mm: float,
    k_air: float,
    calibration: float = 1.0,
) -> MagneticResult:
    load_line = mag_t_mm / (mag_t_mm + air_gap_mm)
    b_gap = br_t * load_line * k_air * calibration
    area_mm2 = mag_w_mm * mag_l_mm
    flux = b_gap * area_mm2 * 1e-6
    return MagneticResult(
        b_gap_t=b_gap,
        pole_area_mm2=area_mm2,
        flux_per_pole_wb=flux,
    )
