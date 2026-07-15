"""2D top-view cross-section of the motor, drawn with Plotly from live params.

Schematic, not CAD-accurate: shows tooth/gap/magnet proportions so geometry
slider changes are visible, with the air gap dimension called out.
"""

from __future__ import annotations

import math

import numpy as np
import plotly.graph_objects as go

from ..models.motor import MotorParams, Performance

COL_STATOR = "#3d5a6c"
COL_COIL = "#c46a2b"
COL_MAG_N = "#b6444a"
COL_MAG_S = "#3f7f56"
COL_ROTOR = "#5a6772"
COL_GAP = "#e8b84b"
COL_TEXT = "#dfe7ec"


def _arc(r: float, a0: float, a1: float, n: int = 40) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(a0, a1, n)
    return r * np.cos(t), r * np.sin(t)


def _closed_ring_sector(r_in, r_out, a0, a1, n=40):
    """Polygon path for a sector of an annulus."""
    xo, yo = _arc(r_out, a0, a1, n)
    xi, yi = _arc(r_in, a1, a0, n)
    x = np.concatenate([xo, xi, [xo[0]]])
    y = np.concatenate([yo, yi, [yo[0]]])
    return x, y


def _poly_trace(x, y, color, name, opacity=1.0, hover=None):
    return go.Scatter(
        x=x,
        y=y,
        fill="toself",
        mode="lines",
        line={"color": color, "width": 1},
        fillcolor=color,
        opacity=opacity,
        name=name,
        hoverinfo="text" if hover else "skip",
        text=hover,
        showlegend=False,
    )


def cross_section_figure(p: MotorParams, perf: Performance) -> go.Figure:
    fig = go.Figure()

    tooth_root_r = p.stator_tip_r - p.tip_thick - p.tooth_h
    hub_r = max(tooth_root_r - 2.0, 3.0)
    mag_out_r = p.mag_face_r + p.mag_t
    rotor_out_r = mag_out_r + p.rotor_wall

    # Rotor shell
    x, y = _closed_ring_sector(mag_out_r, rotor_out_r, 0, 2 * math.pi, 160)
    fig.add_trace(_poly_trace(x, y, COL_ROTOR, "rotor", hover=f"Rotor shell — OD {p.rotor_od:.1f} mm"))

    # Magnets (N-S alternating), slight angular gap for the plastic webs
    mag_half_ang = (p.mag_w / 2) / p.mag_face_r  # chord approx as arc
    for k in range(p.n_poles):
        c = 2 * math.pi * k / p.n_poles
        x, y = _closed_ring_sector(p.mag_face_r, mag_out_r, c - mag_half_ang, c + mag_half_ang, 30)
        pol = "N" if k % 2 == 0 else "S"
        col = COL_MAG_N if pol == "N" else COL_MAG_S
        fig.add_trace(
            _poly_trace(x, y, col, f"magnet {pol}", hover=f"Magnet {pol} — {p.mag_t:.2f} mm thick, face {p.mag_w:.2f} mm")
        )
        lr = mag_out_r + p.rotor_wall / 2 + 2.5
        fig.add_annotation(
            x=lr * math.cos(c), y=lr * math.sin(c), text=pol, showarrow=False,
            font={"color": COL_MAG_N if pol == "N" else COL_MAG_S, "size": 14, "family": "monospace"},
        )

    # Stator hub
    x, y = _closed_ring_sector(hub_r * 0.35, hub_r, 0, 2 * math.pi, 120)
    fig.add_trace(_poly_trace(x, y, COL_STATOR, "hub", hover="Stator hub"))

    # Teeth + coils
    coil_build = min(perf.winding.coil_build_mm, p.tooth_h)
    for k in range(p.n_slots):
        c = 2 * math.pi * k / p.n_slots
        stem_half_ang_root = (p.tooth_stem_w / 2) / max(tooth_root_r, 1e-6)
        stem_half_ang_tip = (p.tooth_stem_w / 2) / (p.stator_tip_r - p.tip_thick)

        # stem
        x, y = _closed_ring_sector(hub_r, p.stator_tip_r - p.tip_thick, c - stem_half_ang_root, c + stem_half_ang_root, 12)
        fig.add_trace(_poly_trace(x, y, COL_STATOR, "tooth", hover=f"Tooth stem — {p.tooth_stem_w:.1f} mm wide"))

        # tip shoe with overhang
        tip_half_ang = stem_half_ang_tip + (1.5 / p.stator_tip_r)
        x, y = _closed_ring_sector(p.stator_tip_r - p.tip_thick, p.stator_tip_r, c - tip_half_ang, c + tip_half_ang, 20)
        fig.add_trace(_poly_trace(x, y, COL_STATOR, "tip", hover="Tooth tip shoe"))

        # coil (drawn as two side bundles proportional to radial build)
        r0 = tooth_root_r + (p.tooth_h - coil_build) / 2
        r1 = r0 + coil_build
        for side in (-1, 1):
            a0 = c + side * stem_half_ang_root
            a1 = c + side * (stem_half_ang_root + (coil_build * 0.9) / max(r0, 1e-6))
            lo, hi = (a0, a1) if a1 > a0 else (a1, a0)
            x, y = _closed_ring_sector(r0, r1, lo, hi, 10)
            fig.add_trace(
                _poly_trace(
                    x, y, COL_COIL, "coil", opacity=0.95,
                    hover=(
                        f"Coil — {p.turns_per_tooth} turns of AWG {p.awg}"
                        f"<br>{perf.winding.n_layers} layers, build {perf.winding.coil_build_mm:.1f} mm"
                    ),
                )
            )

    # Air-gap callout (between tooth tip and magnet face, at 90 deg)
    ang = math.pi / 2 + math.pi / p.n_slots
    xg0, yg0 = p.stator_tip_r * math.cos(ang), p.stator_tip_r * math.sin(ang)
    xg1, yg1 = p.mag_face_r * math.cos(ang), p.mag_face_r * math.sin(ang)
    fig.add_trace(
        go.Scatter(
            x=[xg0, xg1], y=[yg0, yg1], mode="lines",
            line={"color": COL_GAP, "width": 3}, hoverinfo="skip", showlegend=False,
        )
    )
    fig.add_annotation(
        x=(p.mag_face_r + 6) * math.cos(ang), y=(p.mag_face_r + 6) * math.sin(ang),
        text=f"air gap {p.air_gap:.1f} mm", showarrow=False,
        font={"color": COL_GAP, "size": 12},
    )

    # Legend proxies
    for name, col in [("Stator (plastic)", COL_STATOR), ("Coil", COL_COIL), ("Magnet N", COL_MAG_N), ("Magnet S", COL_MAG_S), ("Rotor shell", COL_ROTOR)]:
        fig.add_trace(
            go.Scatter(x=[None], y=[None], mode="markers", marker={"color": col, "size": 10, "symbol": "square"}, name=name)
        )

    lim = rotor_out_r + 8
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis={"visible": False, "range": [-lim, lim], "scaleanchor": "y"},
        yaxis={"visible": False, "range": [-lim, lim]},
        margin={"l": 10, "r": 10, "t": 10, "b": 10},
        height=430,
        legend={"orientation": "h", "y": -0.05, "font": {"color": COL_TEXT, "size": 11}},
    )
    return fig
