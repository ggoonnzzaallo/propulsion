# 3N4P — V2 (planned)

**Status:** Not built yet. Goal: fix V1’s **too-low back-EMF** so a sensorless ESC can lock and spin.

### CAD (Onshape)

**V2 document:** [BLDC V2 — Onshape](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e)

Baseline mechanical design: keep V1 topology (3N4P, Architecture A, same magnets/bearings) unless a reprint is required for gap or winding window.

---

## Problem statement (from V1)

Hand-spin BEMF was only ~**0.2–1 mV** AC phase-to-phase → ESC jerks, never runs.  
See [V1 log](../v1/).

## Primary changes (proposed)

| Change | Why | Notes |
|--------|-----|--------|
| **Many more turns** per tooth | BEMF ∝ turns | Target **100–150+** turns/tooth (tune to fit) |
| **Thinner wire** if needed | Fit more turns in the same window | Prefer **28–30 AWG** if 24 AWG fills too fast |
| Optional **tighter air gap** (~1.0 mm) | Stronger coupling | Only if shaft concentricity improves (true Ø3 shaft) |
| Optional **reprint** stator/rotor | More winding space or gap change | Reuse V1 base if mates still match |

## Keep from V1

- 3N4P, N–S–N–S magnets (4 of 12)
- Star: starts = neutral, ends → ESC; same wind direction on all teeth
- Architecture A mount concept
- Onshape variable-driven CAD

## Explicitly deprioritized (for now)

- Jumping to 6N8P / more magnet pockets “just to try”
- Iron core / sintered inserts (possible later generation)
- Exhaustive star-flip on V1 (BEMF already rules for V2 priorities)

## Success criteria

- [ ] Hand-spin BEMF clearly measurable on **V / low V**, not only noisy mV
- [ ] ESC runs continuously after arm + throttle (flick assist OK on first try)
- [ ] Notes + photos logged under `v2/` after the test

## When V2 starts

1. Decide wire gauge + target turns (measure remaining slot space on V1 tooth or reprint).  
2. Wind or reprint + rewind.  
3. Repeat BEMF test **before** spending time on endless phase swaps.  
4. Log results in this folder (`photos/`, short test notes).
