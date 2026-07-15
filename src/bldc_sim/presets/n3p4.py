"""3N4P presets matching the locked hardware docs.

Geometry from docs/cad-build-guide.md (measured, LOCKED).
V1 = as built and tested (failed: BEMF ~mV).
V2 draft = builds/3n4p/v2/README.md proposal (more turns, thinner wire, tighter gap).
"""

from __future__ import annotations

from ..models.motor import MotorParams

V1 = MotorParams(
    n_slots=3,
    n_poles=4,
    connection="star",
    stator_tip_r=21.0,
    air_gap=1.5,
    mag_t=2.75,
    mag_w=9.25,
    mag_l=28.82,
    tooth_stem_w=8.0,
    tooth_h=10.0,
    tip_thick=1.0,
    stack_len=31.0,
    rotor_wall=3.0,
    br=1.2,
    k_air=0.05,
    turns_per_tooth=40,
    awg=24,
    packing=0.55,
    v_bus=11.1,
    i_max=10.0,
    hand_spin_rpm=300.0,
    esc_bemf_threshold_v=0.5,
)

V2_DRAFT = MotorParams(
    **{
        **V1.to_dict(),
        "turns_per_tooth": 120,
        "awg": 28,
        "air_gap": 1.0,  # only if a true diameter-3.00 shaft lands
    }
)

PRESETS: dict[str, MotorParams] = {
    "3N4P V1 (as built)": V1,
    "3N4P V2 (draft)": V2_DRAFT,
}
