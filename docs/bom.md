# Bill of Materials — 3N4P outrunner (V1 & V2)

Shared **purchased** components for both [V1](../builds/3n4p/v1/) and [V2](../builds/3n4p/v2/). Only the **3D-printed parts** differ between versions (see CAD links below).

Prices are **USD**, captured from Amazon product pages or saved listings **July 2026**. Amazon changes prices often — verify at the link before budgeting.

---

## Per motor — quantity used

| Item | Qty / motor | Notes |
|------|-------------|--------|
| Neodymium bar magnets | **4** | N–S–N–S; 8 spares in 12-pack |
| Miniature ball bearings (623-2RS) | **2** | In rotor hub/tower |
| Magnet wire (24 AWG) | **~15–25 m** | V1 ~40 T/tooth; V2 more turns — one 4 oz spool covers multiple motors |
| M3 socket head screw | **1** | Shaft (30–50 mm from kit) |
| M3 nut + washers | **1–2 sets** | From same kit |
| 30 A sensorless ESC + servo tester | **1** | Shared test bench gear; one unit drives any motor |
| Printed rotor | **1** | Version-specific STL/Onshape |
| Printed stator | **1** | Version-specific |
| Printed base | **1** | Version-specific |

---

## Purchased parts (Amazon)

| # | Item | Description | Pack | Used / motor | List price (USD) | Amazon |
|---|------|-------------|------|--------------|------------------|--------|
| 1 | **Magnet wire** | BNTECHGO **24 AWG** enameled copper magnet wire, **4 oz** (~204 ft), red, 155 °C | 1 spool | wire length | **$11.39** | [B01NBM0MB5](https://www.amazon.com/dp/B01NBM0MB5) |
| 2 | **Bearings** | HiPicco **623-2RS** miniature deep-groove ball bearings, **ID 3 × OD 10 × W 4 mm**, double rubber sealed, chrome steel (20 pcs) | 20 | **2** | *see listing* | [B0CH2YXWJN](https://www.amazon.com/dp/B0CH2YXWJN) |
| 3 | **Permanent magnets** | MIKEDE neodymium bar magnets, nominal **30 × 10 × 3 mm**, **12 pcs** (measured ~**28.8 × 9.3 × 2.8 mm**) | 12 | **4** | *see listing* | [B0FQJH8Y1P](https://www.amazon.com/dp/B0FQJH8Y1P) |
| 4 | **M3 screw kit** | AvrestYPT **461 pc** M3 socket head cap screw assortment: **30 / 35 / 40 / 45 / 50 mm** + matching nuts & washers, 12.9 alloy steel | 461 | **1 screw + hardware** | *see listing* | [B0FGJ9FRGQ](https://www.amazon.com/dp/B0FGJ9FRGQ) |
| 5 | **ESC + servo tester** | DORHEA **30 A** sensorless brushless ESC with integrated **CCPM servo tester** (potentiometer throttle), DC 12 V class | 1 | **1** (shared) | **$7.99** | [B0GZKJ2BTV](https://www.amazon.com/dp/B0GZKJ2BTV) |

Saved listing PDF: [benchmarking/dys-d2830-1000kv/docs/amazon-listing-esc-servo-tester.pdf](../benchmarking/dys-d2830-1000kv/docs/amazon-listing-esc-servo-tester.pdf)

### Allocated cost per motor (rough)

Only items with a known pack price:

| Line | Calculation | ~USD / motor |
|------|-------------|--------------|
| Wire | $11.39 ÷ ~2 motors per spool (estimate) | **~$5.70** |
| ESC + tester | $7.99 ÷ 1 (one bench setup) | **$7.99** |
| Bearings | (pack price ÷ 20) × 2 | *fill when known* |
| Magnets | (pack price ÷ 12) × 4 | *fill when known* |
| M3 hardware | negligible from 461-pc kit | **~$0** |

**Confirmed subtotal (wire + ESC only): ~$13.70** per motor before bearings, magnets, and filament.

---

## 3D-printed parts (not purchased)

| Item | Qty / motor | Source |
|------|-------------|--------|
| Rotor | 1 | Onshape → export STL |
| Stator | 1 | Onshape → export STL |
| Base / mount | 1 | Onshape → export STL |

| Version | Onshape CAD |
|---------|-------------|
| **V1** | [BLDC V1](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) |
| **V2** | [BLDC V2](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e) |

### Printer

| Setting | Value |
|---------|--------|
| Machine | **Bambu Lab P1S** |
| Material | PETG or PLA (project default: **PETG** recommended) |
| Process | Standard FDM; see [cad-build-guide.md](cad-build-guide.md) for slice starting points |

Filament cost depends on part volume and filament roll price — not tracked here.

---

## Optional / bench (not in Amazon list above)

Used during build but not specified as Amazon purchases:

| Item | Role |
|------|------|
| Epoxy | Glue magnets into rotor pockets |
| Solder + heat shrink | Star neutral joint, phase leads |
| Bullet connectors | Phase wires to ESC (see V1/V2 photos) |
| LiPo / DC supply | Powers ESC (voltage per ESC rating) |
| Multimeter | Continuity, BEMF checks |

---

## Version differences (electrical only)

| | V1 | V2 |
|--|----|----|
| Turns / tooth | ~40 | Higher (see V2 wind photos) |
| Wire | 24 AWG (same spool) | Same spool or finer if rewound |
| Printed geometry | Wider air gap, thicker tips | Tighter gap, 0.5 mm tips, routing features |
| Result | Failed (low BEMF) | **Runs** |

Purchased BOM rows **1–5** are identical for both versions.
