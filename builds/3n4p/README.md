# 3N4P outrunner

3 teeth, 4 magnets — fewest coils for a 3-phase hobby ESC. Outrunner layout (V1/V2 plastic core; V3 adds steel).

| Version | Result | Notes |
|---------|--------|-------|
| [V1](v1/) | Failed | ~40 T, 24 AWG; BEMF ~mV · [CAD](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) |
| [V2](v2/) | **Spins** | Low speed only; hand-start; noisy; &lt;1 min · [CAD](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e) |
| [V3](v3/) | Scoped | Steel lams + back-iron + Ø3 shaft ([JLCCNC](https://jlccnc.com/)); goal 5 min · CAD TBD |

## Docs for this build

- **BOM** — below
- [Assembly](../../docs/assembly-magnets-windings.md) — magnets, windings, ESC hookup (V3 Kapton notes in [v3/](v3/))
- [CAD guide](../../docs/cad-build-guide.md) — locked caliper params & print notes
- [Onshape session](../../docs/onshape-session.md) — walkthrough (optional)

## Parts (BOM)

### V1 / V2 (Amazon + print)

Same purchased hardware for **V1** and **V2**; only the printed rotor / stator / base differ.

Printed on **Bambu Lab P1S** in **PLA** for now (PETG after V3). Prices USD, July 2026 — check Amazon before buying.

| Item | Per motor | Pack | Price | Link |
|------|-----------|------|-------|------|
| 24 AWG magnet wire (4 oz) | ~15–25 m | 1 spool | $11.39 | [B01NBM0MB5](https://www.amazon.com/dp/B01NBM0MB5) |
| 623-2RS bearings (3×10×4 mm) | 2 | 20 | $9.99 | [B0CH2YXWJN](https://www.amazon.com/dp/B0CH2YXWJN) |
| Neodymium bars (~30×10×3 mm, measured ~29×9×3) | 4 | 12 | $9.99 | [B0FQJH8Y1P](https://www.amazon.com/dp/B0FQJH8Y1P) |
| M3 screw kit (30–50 mm + nuts/washers) | 1 shaft set | 461 | $9.99 | [B0FGJ9FRGQ](https://www.amazon.com/dp/B0FGJ9FRGQ) |
| 30 A ESC + servo tester | 1 (bench) | 1 | $7.99 | [B0GZKJ2BTV](https://www.amazon.com/dp/B0GZKJ2BTV) |
| Printed rotor + stator + base | 1 each | — | filament | Onshape → STL |

Also used: epoxy (magnets), solder, bullet connectors, LiPo for ESC.

**V1 vs V2 electrical:** V1 ~40 turns/tooth 24 AWG; V2 more turns, tighter air gap — see build logs.

### V3 additions ([JLCCNC](https://jlccnc.com/))

Reuse magnets, bearings, wire, ESC. Drop the M3 screw as shaft. Add:

| Item | Qty | Notes |
|------|-----|-------|
| CRS tooth laminations (~0.5 mm) | ~40–42 | Sheet laser; stack ≈ 31 mm |
| Steel rotor back-iron ring | 1 | CNC; ~2–2.5 mm wall; magnets on ID |
| Ø3.00 mm steel shaft | 1 | CNC turn; true bearing fit |
| Kapton tape | 1 roll | Tooth insulation before wind |
| Printed hub / cage / base | 1 set | PLA; new CAD — see [V3](v3/) |
