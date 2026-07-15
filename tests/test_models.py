"""Sanity tests for the analytical motor model.

These check scaling laws and bench anchors, not absolute accuracy:
- R grows with turns and with AWG (thinner wire)
- BEMF scales linearly with turns and with flux inputs
- Fill stays physical and grows with turns
- V1 preset reproduces its measured behavior: ~0.2 ohm-ish leads and
  hand-spin BEMF far below any ESC lock threshold
"""

import dataclasses

import pytest

from bldc_sim.models.motor import bemf_curve, solve, torque_speed_curve
from bldc_sim.models.winding import awg_diameter_mm, copper_area_mm2
from bldc_sim.presets.n3p4 import V1, V2_DRAFT


def variant(base, **overrides):
    return dataclasses.replace(base, **overrides)


class TestWindingScaling:
    def test_resistance_scales_superlinearly_with_turns(self):
        r1 = solve(variant(V1, turns_per_tooth=40)).winding.r_phase_ohm
        r2 = solve(variant(V1, turns_per_tooth=80)).winding.r_phase_ohm
        # Doubling turns at least doubles R (coil build-up lengthens outer turns).
        assert r2 >= 2 * r1

    def test_thinner_wire_raises_resistance(self):
        r24 = solve(variant(V1, awg=24)).winding.r_phase_ohm
        r30 = solve(variant(V1, awg=30)).winding.r_phase_ohm
        # 6 AWG steps = ~4x area ratio, so ~4x resistance (plus build effects).
        assert r30 > 3.5 * r24

    def test_awg_table_sane(self):
        assert awg_diameter_mm(24) == pytest.approx(0.511, abs=0.01)
        assert copper_area_mm2(20) > copper_area_mm2(30)

    def test_fill_grows_with_turns_and_stays_physical(self):
        f40 = solve(variant(V1, turns_per_tooth=40)).winding.fill_of_packing
        f120 = solve(variant(V1, turns_per_tooth=120)).winding.fill_of_packing
        assert 0 < f40 < f120
        assert f40 == pytest.approx(f120 / 3, rel=1e-6)  # fill linear in turns

    def test_v1_fill_fits(self):
        assert solve(V1).winding.fill_of_packing < 1.0


class TestBemfScaling:
    def test_bemf_linear_in_turns(self):
        e1 = solve(variant(V1, turns_per_tooth=40)).bemf_ll_at_hand_spin
        e2 = solve(variant(V1, turns_per_tooth=80)).bemf_ll_at_hand_spin
        assert e2 == pytest.approx(2 * e1, rel=1e-9)

    def test_bemf_linear_in_br_and_calibration(self):
        base = solve(V1).bemf_ll_at_hand_spin
        assert solve(variant(V1, br=0.6)).bemf_ll_at_hand_spin == pytest.approx(base / 2, rel=1e-9)
        assert solve(variant(V1, calibration=2.0)).bemf_ll_at_hand_spin == pytest.approx(2 * base, rel=1e-9)

    def test_smaller_gap_raises_bemf(self):
        wide = solve(variant(V1, air_gap=1.5)).bemf_ll_at_hand_spin
        tight = solve(variant(V1, air_gap=1.0)).bemf_ll_at_hand_spin
        assert tight > wide

    def test_bemf_curve_monotonic(self):
        p = V1
        perf = solve(p)
        _, e_ph, e_ll = bemf_curve(p, perf)
        assert (e_ll[1:] >= e_ll[:-1]).all()
        assert (e_ll >= e_ph).all()  # star: line-line = sqrt(3) x phase


class TestBenchAnchors:
    """The model must reproduce what the V1 bench test actually showed."""

    def test_v1_lead_resistance_near_measured(self):
        # Measured ~0.2 ohm between ESC leads; accept the right order of magnitude.
        r = solve(V1).winding.r_terminal_ohm
        assert 0.1 < r < 1.0

    def test_v1_bemf_far_below_esc_threshold(self):
        perf = solve(V1)
        assert perf.bemf_ll_at_hand_spin < 0.2 * V1.esc_bemf_threshold_v
        assert perf.esc_verdict == "fail"

    def test_v2_improves_on_v1(self):
        p1, p2 = solve(V1), solve(V2_DRAFT)
        assert p2.bemf_ll_at_hand_spin > 3 * p1.bemf_ll_at_hand_spin
        assert p2.winding.fill_of_packing < 1.0  # proposed wind must fit


class TestTorqueSpeed:
    def test_torque_zero_at_no_load(self):
        p = V1
        perf = solve(p)
        rpm, torque, current = torque_speed_curve(p, perf)
        assert torque[-1] == pytest.approx(0.0, abs=1e-6)
        assert current.max() <= p.i_max + 1e-9

    def test_stall_respects_current_limit(self):
        perf = solve(variant(V1, i_max=5.0))
        assert perf.stall_current <= 5.0
