"""Winding model: wire tables, phase resistance, and slot fill.

All lengths in mm unless suffixed otherwise; resistance in ohms.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

COPPER_RESISTIVITY_OHM_M = 1.724e-8

AWG_CHOICES = list(range(20, 35))


def awg_diameter_mm(awg: int) -> float:
    """Bare copper diameter from the standard AWG formula."""
    return 0.127 * 92 ** ((36 - awg) / 39)


def copper_area_mm2(awg: int) -> float:
    d = awg_diameter_mm(awg)
    return math.pi * d**2 / 4


def resistance_per_m(awg: int) -> float:
    """Ohms per metre of bare copper at 20 C."""
    return COPPER_RESISTIVITY_OHM_M / (copper_area_mm2(awg) * 1e-6)


@dataclass(frozen=True)
class WindingResult:
    wire_d_mm: float
    copper_area_mm2: float
    mean_turn_len_mm: float
    wire_len_m: float
    r_phase_ohm: float
    r_terminal_ohm: float  # what a meter reads across two ESC leads
    window_area_mm2: float
    copper_in_window_mm2: float
    bare_fill: float  # copper area / window area
    fill_of_packing: float  # bare_fill / achievable packing factor
    turns_per_layer: int
    n_layers: int
    coil_build_mm: float


def solve_winding(
    *,
    turns_per_tooth: int,
    awg: int,
    packing: float,
    n_slots: int,
    stator_tip_r_mm: float,
    tip_thick_mm: float,
    tooth_stem_w_mm: float,
    tooth_h_mm: float,
    stack_len_mm: float,
    connection: str,
) -> WindingResult:
    """One coil per phase (one tooth per phase), coils in series per phase = 1.

    Mean turn length wraps the tooth stem cross-section (stem width x stack
    length) and grows with radial coil build-up: offsetting a rectangular
    perimeter by b adds 2*pi*b.
    """
    d = awg_diameter_mm(awg)
    a_cu = copper_area_mm2(awg)

    turns_per_layer = max(1, math.floor(tooth_h_mm / d))
    n_layers = math.ceil(turns_per_tooth / turns_per_layer)
    build = n_layers * d

    base_perimeter = 2 * (tooth_stem_w_mm + stack_len_mm)
    mean_turn_len = base_perimeter + math.pi * build  # offset by build/2 on average

    wire_len_m = turns_per_tooth * mean_turn_len / 1000
    r_phase = wire_len_m * resistance_per_m(awg)

    # Terminal (lead-to-lead) resistance as a multimeter would read it.
    if connection == "star":
        r_terminal = 2 * r_phase
    else:  # delta: one phase in parallel with the other two in series
        r_terminal = (r_phase * 2 * r_phase) / (3 * r_phase)

    # Winding window: circumferential space between stems at mid tooth height,
    # split between the two coil sides sharing each slot.
    mid_r = stator_tip_r_mm - tip_thick_mm - tooth_h_mm / 2
    slot_space = (2 * math.pi * mid_r - n_slots * tooth_stem_w_mm) / n_slots
    per_side_w = slot_space / 2
    window_area = tooth_h_mm * per_side_w

    copper_in_window = turns_per_tooth * a_cu
    bare_fill = copper_in_window / window_area
    fill_of_packing = bare_fill / packing

    return WindingResult(
        wire_d_mm=d,
        copper_area_mm2=a_cu,
        mean_turn_len_mm=mean_turn_len,
        wire_len_m=wire_len_m,
        r_phase_ohm=r_phase,
        r_terminal_ohm=r_terminal,
        window_area_mm2=window_area,
        copper_in_window_mm2=copper_in_window,
        bare_fill=bare_fill,
        fill_of_packing=fill_of_packing,
        turns_per_layer=turns_per_layer,
        n_layers=n_layers,
        coil_build_mm=build,
    )
