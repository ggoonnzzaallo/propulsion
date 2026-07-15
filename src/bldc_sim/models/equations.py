"""Equation metadata for the in-app Learn panels.

Each entry pairs the LaTeX used by the model with a symbol glossary and a
one-line intuition, so the UI can teach the physics next to the numbers.
Keep in sync with magnetic.py / winding.py / motor.py.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Equation:
    title: str
    latex: str
    symbols: dict[str, str]  # symbol (latex ok) -> meaning with units
    sliders: list[str]  # which UI inputs appear in this equation
    intuition: str
    extra_latex: list[str] = field(default_factory=list)


EQUATIONS: dict[str, Equation] = {
    "flux": Equation(
        title="Air-gap flux per pole",
        latex=r"\Phi = B_\mathrm{gap}\, A_\mathrm{mag}, \qquad B_\mathrm{gap} = k_\mathrm{air}\, B_r\,\frac{t_m}{t_m + g}",
        symbols={
            r"\Phi": "magnetic flux per pole (Wb)",
            r"B_r": "magnet remanence (T), ~1.2 T for NdFeB",
            r"t_m": "magnet radial thickness (mm)",
            r"g": "air gap (mm)",
            r"k_\mathrm{air}": "air-core derating — plastic stator has no iron flux return path",
            r"A_\mathrm{mag}": "magnet face area = width x length (m^2)",
        },
        sliders=["Remanence Br", "Air gap", "Magnet dimensions", "Air-core derating"],
        intuition=(
            "The magnet's field divides between crossing the gap and leaking sideways. "
            "A thicker magnet or smaller gap pushes more flux through the coil; without iron, "
            "most of it never makes the trip — that is k_air, and it is why V1 measured millivolts."
        ),
    ),
    "bemf": Equation(
        title="Back-EMF and Ke",
        latex=r"e_\mathrm{ph} = N_t\,\Phi\,\omega_e = \underbrace{N_t\,\Phi\,p}_{K_e}\;\omega_m",
        extra_latex=[
            r"\omega_e = p\,\omega_m, \qquad p = \tfrac{P}{2} \text{ (pole pairs)}",
            r"E_\mathrm{LL} = \sqrt{3}\,e_\mathrm{ph} \;\text{(star)} \qquad E_\mathrm{LL} = e_\mathrm{ph} \;\text{(delta)}",
        ],
        symbols={
            r"e_\mathrm{ph}": "peak phase back-EMF (V)",
            r"N_t": "turns per tooth",
            r"\Phi": "flux per pole (Wb)",
            r"\omega_m,\ \omega_e": "mechanical / electrical speed (rad/s)",
            r"P": "number of magnet poles",
            r"K_e": "back-EMF constant (V*s/rad)",
        },
        sliders=["Turns per tooth", "Poles", "Star/delta", "everything feeding flux"],
        intuition=(
            "Faraday's law: volts = turns x flux x how fast the flux flips. Double the turns, "
            "double the BEMF at the same RPM. This is the single most direct fix for V1's ESC lock failure."
        ),
    ),
    "kt": Equation(
        title="Torque constant",
        latex=r"\tau = K_t\, I, \qquad K_t = \tfrac{3}{2}\,K_{e,\mathrm{ph}} \;\;\text{(sinusoidal, SI units)}",
        symbols={
            r"\tau": "shaft torque (N*m)",
            r"I": "peak phase current (A)",
            r"K_t": "torque constant (N*m/A)",
            r"K_{e,\mathrm{ph}}": "per-phase back-EMF constant (V*s/rad)",
        },
        sliders=["same as Ke — they are two faces of one constant"],
        intuition=(
            "Ke and Kt are the same physics seen from two sides (energy conservation): "
            "a motor that generates more volts per RPM also makes more torque per amp. "
            "You cannot raise one without the other."
        ),
    ),
    "resistance": Equation(
        title="Phase resistance",
        latex=r"R_\mathrm{ph} = \rho_\mathrm{cu}\,\frac{\ell}{A_\mathrm{cu}}, \qquad \ell = N_t \times \ell_\mathrm{turn}",
        symbols={
            r"\rho_\mathrm{cu}": "copper resistivity, 1.724e-8 ohm*m at 20 C",
            r"\ell": "total wire length in one phase (m)",
            r"\ell_\mathrm{turn}": "mean length of one turn around the tooth (grows as the coil builds up)",
            r"A_\mathrm{cu}": "bare copper cross-section from AWG (m^2)",
        },
        sliders=["Turns per tooth", "Wire AWG", "Tooth stem width", "Stack length"],
        intuition=(
            "More turns = more wire = more resistance; thinner wire (higher AWG) has less copper area, "
            "so R rises fast — every 3 AWG steps roughly doubles it. This is the price you pay for BEMF."
        ),
    ),
    "fill": Equation(
        title="Slot fill",
        latex=r"\mathrm{fill} = \frac{N_t\,A_\mathrm{cu}}{\eta_\mathrm{pack}\,A_\mathrm{window}}",
        symbols={
            r"N_t": "turns per tooth",
            r"A_\mathrm{cu}": "copper cross-section of one strand (mm^2)",
            r"A_\mathrm{window}": "winding window area beside the tooth (mm^2)",
            r"\eta_\mathrm{pack}": "achievable packing factor (~0.5-0.6 hand-wound round wire)",
        },
        sliders=["Turns per tooth", "Wire AWG", "Tooth height", "Tooth stem width", "Packing factor"],
        intuition=(
            "Physics says wind more turns; geometry says they must fit. Above ~100% the coil "
            "physically will not fit the slot — drop to thinner wire or reprint with a bigger window."
        ),
    ),
    "torque_speed": Equation(
        title="Torque-speed line",
        latex=r"\tau(\omega) = K_t\,\min\!\left(\frac{V - K_{e,\mathrm{LL}}\,\omega}{R_\mathrm{drive}},\; I_\mathrm{max}\right)",
        symbols={
            r"V": "bus voltage (V)",
            r"K_{e,\mathrm{LL}}": "line-line back-EMF constant (V*s/rad)",
            r"R_\mathrm{drive}": "resistance the ESC drives through (2 R_ph in star)",
            r"I_\mathrm{max}": "current limit (A)",
            r"\omega": "mechanical speed (rad/s)",
        },
        sliders=["Bus voltage", "Current limit", "everything feeding Ke and R"],
        intuition=(
            "At stall all of V drives current; as the motor spins up, BEMF pushes back and current "
            "falls, hitting zero torque at no-load speed V/Ke. The flat top is the current limit."
        ),
    ),
    "copper_loss": Equation(
        title="Copper loss",
        latex=r"P_\mathrm{cu} = I^2\,R_\mathrm{drive}",
        symbols={
            r"P_\mathrm{cu}": "heat dissipated in the winding (W)",
            r"I": "drive current (A)",
            r"R_\mathrm{drive}": "conducting-path resistance (ohm)",
        },
        sliders=["Current limit", "everything feeding R"],
        intuition=(
            "Heat grows with the square of current. High-turn thin-wire windings trade copper loss "
            "for BEMF — fine for a low-power demo, decisive at high power. PETG softens near 80 C."
        ),
    ),
    "esc": Equation(
        title="ESC lock check",
        latex=r"E_\mathrm{LL}(n_\mathrm{spin}) \gtrsim E_\mathrm{thresh} \;\Rightarrow\; \text{sensorless ESC can commutate}",
        symbols={
            r"n_\mathrm{spin}": "hand-spin speed (RPM)",
            r"E_\mathrm{LL}": "peak line-line BEMF at that speed (V)",
            r"E_\mathrm{thresh}": "detection threshold, typically ~0.5-1 V for hobby ESCs",
        },
        sliders=["Hand-spin RPM", "ESC threshold", "everything feeding Ke"],
        intuition=(
            "A sensorless ESC finds the rotor by reading BEMF zero-crossings on the undriven phase. "
            "V1's ~1 mV was pure noise to it — hence jerk, no run. This card is the multimeter test, predicted."
        ),
    ),
}
