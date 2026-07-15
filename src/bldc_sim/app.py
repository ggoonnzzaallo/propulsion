"""BLDC parameter simulator — Streamlit app.

Run: uv run streamlit run src/bldc_sim/app.py
"""

from __future__ import annotations

import dataclasses

import plotly.graph_objects as go
import streamlit as st

from bldc_sim.geometry.cross_section import cross_section_figure
from bldc_sim.models.equations import EQUATIONS, Equation
from bldc_sim.models.motor import (
    MotorParams,
    Performance,
    bemf_curve,
    copper_loss_curve,
    solve,
    torque_speed_curve,
)
from bldc_sim.models.winding import AWG_CHOICES
from bldc_sim.presets.n3p4 import PRESETS

# ---------------------------------------------------------------- theme

ACCENT = "#e8b84b"
ACCENT_2 = "#c46a2b"
BG = "#141a1f"
PANEL = "#1c242b"
TEXT = "#dfe7ec"
MUTED = "#8fa1ad"
PASS = "#4caf6e"
MARGINAL = "#e8b84b"
FAIL = "#d9534f"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

html, body, [class*="css"], .stApp {{
    font-family: 'Space Grotesk', sans-serif;
}}
.stApp {{
    background: radial-gradient(1200px 600px at 15% -10%, #223039 0%, {BG} 55%) fixed;
    color: {TEXT};
}}
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #18212800, #18212855), {PANEL};
    border-right: 1px solid #2b3640;
}}
[data-testid="stSidebar"] .stMarkdown h2 {{
    font-size: 0.85rem; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED};
}}
h1, h2, h3 {{ color: {TEXT}; }}
.brand-title {{
    font-size: 2.1rem; font-weight: 700; letter-spacing: 0.01em; line-height: 1.1;
    color: {TEXT}; margin-bottom: 0;
}}
.brand-title .accent {{ color: {ACCENT}; }}
.brand-sub {{ color: {MUTED}; margin-top: 0.15rem; font-size: 0.95rem; }}
.kpi-card {{
    background: {PANEL}; border: 1px solid #2b3640; border-radius: 10px;
    padding: 0.7rem 0.9rem; height: 100%;
}}
.kpi-label {{
    font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED};
    font-family: 'IBM Plex Mono', monospace;
}}
.kpi-value {{
    font-size: 1.35rem; font-weight: 700; color: {TEXT}; font-family: 'IBM Plex Mono', monospace;
    margin-top: 0.1rem;
}}
.kpi-unit {{ font-size: 0.75rem; color: {MUTED}; font-weight: 400; }}
.kpi-note {{ font-size: 0.72rem; color: {MUTED}; margin-top: 0.15rem; }}
.verdict-pass {{ color: {PASS}; }}
.verdict-marginal {{ color: {MARGINAL}; }}
.verdict-fail {{ color: {FAIL}; }}
.kpi-card.v-pass {{ border-color: {PASS}66; box-shadow: 0 0 0 1px {PASS}33 inset; }}
.kpi-card.v-marginal {{ border-color: {MARGINAL}66; box-shadow: 0 0 0 1px {MARGINAL}33 inset; }}
.kpi-card.v-fail {{ border-color: {FAIL}66; box-shadow: 0 0 0 1px {FAIL}33 inset; }}
div[data-testid="stExpander"] {{
    background: {PANEL}; border: 1px solid #2b3640; border-radius: 10px;
}}
div[data-testid="stExpander"] summary {{ color: {ACCENT}; }}
.stButton > button {{
    background: {PANEL}; color: {TEXT}; border: 1px solid #3a4855; border-radius: 8px;
}}
.stButton > button:hover {{ border-color: {ACCENT}; color: {ACCENT}; }}
hr {{ border-color: #2b3640; }}
</style>
"""

PLOT_LAYOUT = {
    "template": "plotly_dark",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(28,36,43,0.6)",
    "font": {"family": "Space Grotesk, sans-serif", "color": TEXT, "size": 12},
    "margin": {"l": 50, "r": 20, "t": 40, "b": 45},
    "height": 320,
    "hovermode": "x unified",
}

# ---------------------------------------------------------------- helpers

FIELDS = {f.name for f in dataclasses.fields(MotorParams)}


def apply_preset(preset: MotorParams) -> None:
    for k, v in preset.to_dict().items():
        st.session_state[f"p_{k}"] = v


def params_from_state() -> MotorParams:
    kwargs = {}
    for name in FIELDS:
        key = f"p_{name}"
        if key in st.session_state:
            kwargs[name] = st.session_state[key]
    return MotorParams(**kwargs)


def kpi(col, label: str, value: str, unit: str = "", note: str = "", verdict: str = "") -> None:
    cls = f"kpi-card v-{verdict}" if verdict else "kpi-card"
    col.markdown(
        f'<div class="{cls}"><div class="kpi-label">{label}</div>'
        f'<div class="kpi-value">{value} <span class="kpi-unit">{unit}</span></div>'
        f'<div class="kpi-note">{note}</div></div>',
        unsafe_allow_html=True,
    )


def learn_panel(eq: Equation) -> None:
    with st.expander(f"Learn — {eq.title}"):
        st.latex(eq.latex)
        for extra in eq.extra_latex:
            st.latex(extra)
        rows = "".join(
            f"| ${sym}$ | {meaning} |\n" for sym, meaning in eq.symbols.items()
        )
        st.markdown("| Symbol | Meaning |\n|---|---|\n" + rows)
        st.markdown(f"**Inputs that move this:** {', '.join(eq.sliders)}")
        st.markdown(f"*{eq.intuition}*")


# ---------------------------------------------------------------- page

st.set_page_config(page_title="BLDC Lab — 3N4P Simulator", page_icon="🧲", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

if "p_turns_per_tooth" not in st.session_state:
    apply_preset(PRESETS["3N4P V1 (as built)"])

# ------------------------------------------------ sidebar (inputs)

with st.sidebar:
    st.markdown("## Presets")
    cols = st.columns(2)
    for col, (name, preset) in zip(cols, PRESETS.items()):
        if col.button(name.replace("3N4P ", ""), use_container_width=True):
            apply_preset(preset)
            st.rerun()

    st.markdown("## Topology")
    st.number_input("Slots (teeth)", 3, 12, step=3, key="p_n_slots")
    st.number_input("Magnet poles", 2, 14, step=2, key="p_n_poles")
    st.radio("Connection", ["star", "delta"], key="p_connection", horizontal=True)

    st.markdown("## Geometry (mm)")
    st.slider("Stator tip radius", 10.0, 40.0, step=0.5, key="p_stator_tip_r")
    st.slider("Air gap", 0.5, 3.0, step=0.1, key="p_air_gap")
    st.slider("Tooth stem width", 4.0, 16.0, step=0.5, key="p_tooth_stem_w")
    st.slider("Tooth height (winding depth)", 5.0, 20.0, step=0.5, key="p_tooth_h")
    st.slider("Stack length", 10.0, 50.0, step=0.5, key="p_stack_len")
    with st.expander("Magnet dimensions"):
        st.slider("Magnet thickness (radial)", 1.0, 6.0, step=0.05, key="p_mag_t")
        st.slider("Magnet width (chord)", 4.0, 20.0, step=0.05, key="p_mag_w")
        st.slider("Magnet length (axial)", 10.0, 50.0, step=0.1, key="p_mag_l")

    st.markdown("## Magnets")
    st.slider("Remanence Br (T)", 0.4, 1.5, step=0.05, key="p_br",
              help="NdFeB ~1.2 T, ferrite ~0.4 T")
    st.slider("Air-core derating k_air", 0.01, 1.0, step=0.01, key="p_k_air",
              help="Fraction of ideal iron-core flux that links the coil. Plastic stator + plastic rotor back ≈ 0.03–0.1. Set to 1.0 to see what iron would buy you.")
    st.slider("Calibration scale", 0.1, 3.0, step=0.05, key="p_calibration",
              help="Multiply predicted BEMF to anchor the model to a bench measurement.")

    st.markdown("## Winding")
    st.slider("Turns per tooth", 5, 400, step=5, key="p_turns_per_tooth")
    st.select_slider("Wire gauge (AWG)", options=AWG_CHOICES, key="p_awg",
                     help="Bigger AWG number = thinner wire")
    st.slider("Packing factor", 0.3, 0.8, step=0.05, key="p_packing",
              help="Fraction of the window a hand-wound round-wire coil can realistically fill")

    st.markdown("## Drive / test")
    st.slider("Bus voltage (V)", 3.7, 25.2, step=0.1, key="p_v_bus")
    st.slider("Current limit (A)", 1.0, 40.0, step=0.5, key="p_i_max")
    st.slider("Hand-spin speed (RPM)", 60.0, 1000.0, step=10.0, key="p_hand_spin_rpm")
    st.slider("ESC BEMF threshold (V)", 0.1, 2.0, step=0.1, key="p_esc_bemf_threshold_v",
              help="Line-line BEMF a sensorless ESC needs to detect zero-crossings; ~0.5–1 V for hobby ESCs")
    st.slider("Chart RPM range", 1000.0, 20000.0, step=500.0, key="p_rpm_max")

p = params_from_state()
perf = solve(p)
w = perf.winding
m = perf.magnetic

# ------------------------------------------------ header

st.markdown(
    '<div class="brand-title">BLDC <span class="accent">Lab</span></div>'
    '<div class="brand-sub">Analytical parameter explorer for the air-core 3N4P outrunner — '
    'every number links back to the equation that made it.</div>',
    unsafe_allow_html=True,
)
st.markdown("")

# ------------------------------------------------ KPI row

verdict_text = {"pass": "ESC should lock", "marginal": "Borderline", "fail": "ESC cannot see it"}
verdict_note = {
    "pass": "BEMF above detection threshold",
    "marginal": "Within 2x of threshold — risky",
    "fail": "Raise turns, shrink gap, or add flux",
}

c = st.columns(6)
kpi(c[0], "Flux / pole", f"{m.flux_per_pole_wb * 1e6:.1f}", "µWb",
    f"B_gap ≈ {m.b_gap_t * 1e3:.1f} mT")
kpi(c[1], "Ke (line-line)", f"{perf.ke_ll * 1e3:.2f}", "mV·s/rad",
    f"Kv ≈ {perf.kv_rpm_per_v:,.0f} RPM/V")
kpi(c[2], "Kt", f"{perf.kt * 1e3:.2f}", "mN·m/A",
    f"stall ≈ {perf.stall_torque * 1e3:.1f} mN·m @ {perf.stall_current:.1f} A")
kpi(c[3], "Phase R", f"{w.r_phase_ohm:.2f}", "Ω",
    f"meter reads {w.r_terminal_ohm:.2f} Ω lead-to-lead")
fill_pct = w.fill_of_packing * 100
kpi(c[4], "Slot fill", f"{fill_pct:.0f}", "%",
    f"{w.n_layers} layers, build {w.coil_build_mm:.1f} mm" if fill_pct <= 100 else "Does not fit — thinner wire or bigger window",
    verdict="" if fill_pct <= 100 else "fail")
bemf_mv = perf.bemf_ll_at_hand_spin * 1e3
bemf_str = f"{bemf_mv:.1f} mV" if bemf_mv < 1000 else f"{bemf_mv / 1000:.2f} V"
kpi(c[5], f"BEMF @ {p.hand_spin_rpm:.0f} RPM", bemf_str.split(" ")[0], bemf_str.split(" ")[1],
    f"{verdict_text[perf.esc_verdict]} — {verdict_note[perf.esc_verdict]}",
    verdict=perf.esc_verdict)

st.markdown("")

# ------------------------------------------------ charts + geometry

tab_perf, tab_geom, tab_learn = st.tabs(["Performance", "Geometry", "Learn the physics"])

with tab_perf:
    col1, col2 = st.columns(2)

    rpm, e_ph, e_ll = bemf_curve(p, perf)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rpm, y=e_ll, name="Line-line (peak)", line={"color": ACCENT, "width": 3}))
    fig.add_trace(go.Scatter(x=rpm, y=e_ph, name="Phase (peak)", line={"color": ACCENT_2, "width": 2, "dash": "dot"}))
    fig.add_hline(y=p.esc_bemf_threshold_v, line={"color": FAIL, "dash": "dash"},
                  annotation_text="ESC threshold", annotation_font_color=FAIL)
    fig.add_vline(x=p.hand_spin_rpm, line={"color": MUTED, "dash": "dot"},
                  annotation_text="hand spin", annotation_font_color=MUTED)
    fig.update_layout(title="Back-EMF vs speed", xaxis_title="RPM", yaxis_title="BEMF (V)", **PLOT_LAYOUT)
    col1.plotly_chart(fig, use_container_width=True)
    with col1:
        learn_panel(EQUATIONS["bemf"])
        learn_panel(EQUATIONS["esc"])

    rpm_t, torque, current = torque_speed_curve(p, perf)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rpm_t, y=torque * 1e3, name="Torque", line={"color": ACCENT, "width": 3}))
    fig.add_trace(go.Scatter(x=rpm_t, y=current, name="Current", yaxis="y2",
                             line={"color": ACCENT_2, "width": 2, "dash": "dot"}))
    layout = dict(PLOT_LAYOUT)
    layout["margin"] = {**PLOT_LAYOUT["margin"], "r": 55}
    fig.update_layout(
        title=f"Torque-speed @ {p.v_bus:.1f} V, {p.i_max:.0f} A limit",
        xaxis_title="RPM", yaxis_title="Torque (mN·m)",
        yaxis2={"title": "Current (A)", "overlaying": "y", "side": "right", "showgrid": False},
        **layout,
    )
    col2.plotly_chart(fig, use_container_width=True)
    with col2:
        learn_panel(EQUATIONS["torque_speed"])
        learn_panel(EQUATIONS["kt"])

    col3, col4 = st.columns(2)
    i_sweep, p_cu, tq = copper_loss_curve(p, perf)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=i_sweep, y=p_cu, name="Copper loss", line={"color": FAIL, "width": 3}))
    fig.add_trace(go.Scatter(x=i_sweep, y=tq * 1e3, name="Torque", yaxis="y2",
                             line={"color": ACCENT, "width": 2, "dash": "dot"}))
    layout = dict(PLOT_LAYOUT)
    layout["margin"] = {**PLOT_LAYOUT["margin"], "r": 55}
    fig.update_layout(
        title="Copper loss vs load current",
        xaxis_title="Current (A)", yaxis_title="Loss (W)",
        yaxis2={"title": "Torque (mN·m)", "overlaying": "y", "side": "right", "showgrid": False},
        **layout,
    )
    col3.plotly_chart(fig, use_container_width=True)
    with col3:
        learn_panel(EQUATIONS["copper_loss"])

    with col4:
        st.markdown("#### Winding reality check")
        st.markdown(
            f"""
| Quantity | Value |
|---|---|
| Wire diameter | {w.wire_d_mm:.3f} mm (AWG {p.awg}) |
| Mean turn length | {w.mean_turn_len_mm:.1f} mm |
| Wire per coil | {w.wire_len_m:.1f} m |
| Turns per layer | {w.turns_per_layer} |
| Layers | {w.n_layers} |
| Radial build | {w.coil_build_mm:.1f} mm of {p.tooth_h:.1f} mm available |
| Window fill (of packable area) | {fill_pct:.0f}% |
"""
        )
        learn_panel(EQUATIONS["resistance"])
        learn_panel(EQUATIONS["fill"])

with tab_geom:
    gcol, tcol = st.columns([3, 2])
    gcol.plotly_chart(cross_section_figure(p, perf), use_container_width=True)
    with tcol:
        st.markdown("#### Derived geometry")
        st.markdown(
            f"""
| Quantity | Value |
|---|---|
| Magnet face radius | {p.mag_face_r:.2f} mm |
| Rotor OD | {p.rotor_od:.1f} mm |
| Tooth root radius | {p.stator_tip_r - p.tip_thick - p.tooth_h:.1f} mm |
| Winding window (per coil side) | {w.window_area_mm2:.0f} mm² |
| Magnet pole area | {m.pole_area_mm2:.0f} mm² |
"""
        )
        learn_panel(EQUATIONS["flux"])
        st.info(
            "Schematic proportions, not CAD. Slide the air gap or tooth size in the sidebar "
            "and watch the section redraw — the yellow tick marks the gap the flux must cross."
        )

with tab_learn:
    st.markdown(
        "#### The chain from magnet to motion\n"
        "Magnet flux crosses the air gap, links the turns, and sets the two constants "
        "($K_e$, $K_t$) that fix everything else. Work top to bottom:"
    )
    order = ["flux", "bemf", "kt", "resistance", "fill", "torque_speed", "copper_loss", "esc"]
    lcol, rcol = st.columns(2)
    for i, key in enumerate(order):
        with (lcol if i % 2 == 0 else rcol):
            learn_panel(EQUATIONS[key])
    st.markdown(
        "---\n**Bench tie-in:** the *BEMF @ hand-spin* card is exactly the V1 failure test — "
        "ESC disconnected, multimeter on AC across two phase leads, spin the rotor hard. "
        "V1 measured ~0.2–1 mV. Treat the prediction as an optimistic upper bound: real hand "
        "spins are slower than the slider default, and multimeters under-read low-frequency AC. "
        "Once you have a trustworthy measurement, use the *Calibration scale* slider to anchor the model."
    )
