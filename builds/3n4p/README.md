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

**Unit cost** = purchase price ÷ pack quantity. **Cost / motor** = unit cost × qty used.

| Item | Used / motor | Purchase | Unit cost | Cost / motor | Link |
|------|--------------|----------|-----------|--------------|------|
| 24 AWG magnet wire | ~20 m | $11.39 / ~60 m spool (4 oz) | $0.19 / m | $3.80 | [Amazon (US)](https://www.amazon.com/dp/B01NBM0MB5) |
| 623-2RS bearings (3×10×4 mm) | 2 | $9.99 / 20 pcs | $0.50 / pc | $1.00 | [Amazon (US)](https://www.amazon.com/dp/B0CH2YXWJN) |
| Neodymium bars (~30×10×3 mm) | 4 | $9.99 / 12 pcs | $0.83 / pc | $3.33 | [Amazon (US)](https://www.amazon.com/dp/B0FQJH8Y1P) |
| M3 shaft hardware | 5 pcs | $9.99 / 461 pcs | $0.02 / pc | $0.11 | [Amazon (US)](https://www.amazon.com/dp/B0FGJ9FRGQ) |
| 30 A ESC + servo tester | 1 | $7.99 / 1 kit | $7.99 / kit | $7.99 | [Amazon (US)](https://www.amazon.com/dp/B0GZKJ2BTV) |
| Printed rotor + stator + base | 1 set | filament | — | — | Onshape → STL |
| **Total / motor** | | | | **$16.23** | |

Wire spool length ≈ 60 m estimated for 4 oz 24 AWG; used length mid of ~15–25 m. M3 line = 1 long screw + 2 nuts + 2 washers. Cart to buy one of each pack once: **$49.35** (leftovers cover more motors).

Also used (not in total): epoxy, solder, bullet connectors, LiPo, PLA filament.

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
