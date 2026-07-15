# 3N4P — V2

**Status:** CAD in progress (not printed/tested yet). Goal: fix V1’s **too-low back-EMF** so a sensorless ESC can lock and spin.

### CAD (Onshape)

**V2 document:** [BLDC V2 — Onshape](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e)

Still **3N4P**, Architecture A, same magnets/bearings family as V1 — geometry refined for coupling, winding, and assembly.

---

## Problem statement (from V1)

Hand-spin BEMF was only ~**0.2–1 mV** AC phase-to-phase → ESC jerks, never runs.  
See [V1 log](../v1/).

---

## CAD changes so far (vs V1)

| Change | Detail |
|--------|--------|
| **Tighter air gap** | Rotor diameter reduced so magnet↔stator clearance is **under ~1 mm** (measured as **minimum** distance magnet face → stator; value depends on where you measure) |
| **Stator fillets** | Fillets on stator to remove sharp corners for safer / easier coil winding |
| **Rotor visibility cutouts** | Openings in the rotor so the interior (stator, windings, gap) can be seen when assembled |
| **Stator press chamfer** | Chamfer on the stator hub so it presses onto the base more easily |
| **Winding body (CAD)** | Solid body added to **represent** the winding bundle (keep-out / packaging — not literal turns) |
| **Base wire routing** | Features on the base to route phase leads to the ESC and manage the **neutral** joint |

### Still planned (electrical)

| Change | Why |
|--------|-----|
| **Many more turns** / tooth | BEMF ∝ turns — target **100–150+** (tune to fit) |
| **Thinner wire** if needed | Fit more turns — prefer **28–30 AWG** if 24 AWG fills too fast |

Tighter gap helps coupling; **turn count** is still expected to be the main BEMF lever after V1.

Explore candidates in the repo simulator before winding: [`../../docs/simulator.md`](../../docs/simulator.md) (`V2_DRAFT` preset ≈ 120 turns / 28 AWG / ~1 mm gap).

---

## Keep from V1

- 3N4P, N–S–N–S magnets (4 of 12)
- Star: starts = neutral, ends → ESC; same wind direction on all teeth
- Architecture A (stator on base; bearings in rotor)
- Onshape parametric CAD

## Explicitly deprioritized (for now)

- Jumping to 6N8P / more magnet pockets “just to try”
- Iron core / sintered inserts (possible later generation)
- Exhaustive star-flip on leftover V1 hardware as the main path

## Success criteria

- [ ] Hand-spin BEMF clearly measurable on **V / low V**, not only noisy mV
- [ ] ESC runs continuously after arm + throttle (flick assist OK on first try)
- [ ] Notes + photos logged under `v2/` after the test

## Next hardware steps

1. Freeze CAD → export / print coupons (bearing bore, magnet pocket, press-fit chamfer).  
2. Print full V2 set.  
3. Wind for **high turn count**; confirm with BEMF test **before** long phase-swap sessions.  
4. Log results + photos here.
