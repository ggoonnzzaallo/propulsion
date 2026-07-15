# BLDC 3N4P Outrunner — CAD Build Guide (simplest wind)

You have hardware in hand. Goal: model printable **stator**, **rotor**, and **shaft/hub stack**, then export STLs.

Use any parametric CAD (Fusion 360, FreeCAD, Onshape, SolidWorks). Steps are software-agnostic.

---

## Stage 0 — Measured actuals (LOCKED)

Use these caliper values everywhere. Ignore packaging “20×10×3” labels.

| Part | Measured | CAD orientation / name |
|------|----------|------------------------|
| Magnets (12 on hand; **use 4** for 3N4P) | **2.75 × 9.25 × 28.82 mm** | `MAG_T`=2.75 (radial), `MAG_W`=9.25 (chord), `MAG_L`=28.82 (axial) |
| Bearing width | **3.97 mm** | `BRG_W` |
| Bearing OD | **9.96 mm** | `BRG_OD` |
| Bearing ID | **2.99 mm** | `BRG_ID` |
| M3 screw (as measured) | **2.80 mm** | `SHAFT_OD` — see shaft warning below |

**Decide now (write it down):**

- Filament: PETG (recommended) or PLA → `MATERIAL`
- CAD tool: ________________
- Print nozzle: 0.4 mm assumed

### Shaft clearance warning

Bearing ID 2.99 − screw 2.80 = **0.19 mm** diameter clearance (~**0.10 mm** radial play).

That is enough to eat a 1.0 mm air gap if the rotor tilts. Do this before CAD:

1. Re-measure the screw on any **unthreaded shank**. Many SHCS are ~2.9–3.0 mm on the smooth part and only ~2.8 mm on the threads.
2. If the whole screw is ≤2.85 mm, either:
   - Prefer a true **3.00 mm** shaft rod / precision shoulder screw through the bearings, or
   - Widen design air gap to **1.5 mm** for the first print (`STATOR_TIP_R` 21.0 → `MAG_FACE_R` 22.5).

**Default below uses `AIR_GAP` = 1.5 mm** until you confirm a snug ~3.0 mm shaft.

---

## Stage 1 — Create a parameters table (10 min)

Create these user parameters first. Do not sketch freehand numbers.

### Locked design (from your calipers)

| Name | Value | Notes |
|------|-------|-------|
| `AIR_GAP` | **1.5 mm** | Raised for shaft play; drop to 1.0 if shaft is true Ø3.00 |
| `STATOR_TIP_R` | 21.0 mm | Outer radius of tooth tips |
| `MAG_FACE_R` | **22.5 mm** | = `STATOR_TIP_R` + `AIR_GAP` |
| `MAG_L` | **28.82 mm** | Axial (along shaft) |
| `MAG_W` | **9.25 mm** | Chord / pocket width |
| `MAG_T` | **2.75 mm** | Radial thickness |
| `POCKET_L` | **29.05 mm** | Mag length + 0.23 |
| `POCKET_W` | **9.40 mm** | Mag width + 0.15 |
| `POCKET_T` | **2.85 mm** | Mag thickness + 0.10 |
| `ROTOR_WALL` | 3.0 mm | Outside magnets |
| `MAG_WEB` | 2.0 mm | Plastic between magnets |
| `TOOTH_STEM_W` | **8.0 mm** | Wider OK with only 3 teeth — easier winding |
| `TOOTH_H` | 10.0 mm | Radial winding depth |
| `TIP_OVERHANG` | 1.5 mm | Retaining lip each side |
| `TIP_THICK` | 1.0 mm | Lip thickness (radial) |
| `STATOR_STACK` | **31.0 mm** | Magnets ~28.8 + ~1 mm lip each end |
| `N_SLOTS` | **3** | Simplest 3-phase: one coil per phase |
| `N_POLES` | **4** | Use 4 of your 12 magnets |
| `TURNS_PER_TOOTH` | **40** | Fewer teeth → put more turns on each |
| `BRG_OD` | **9.96 mm** | Measured |
| `BRG_W` | **3.97 mm** | Measured |
| `BRG_ID` | **2.99 mm** | Measured |
| `BRG_BORE_PRINT` | **9.85 mm** | Press onto 9.96 OD (FDM shrink) |
| `BRG_BORE_FINAL` | **9.96 mm** | Ideal after press/ream |
| `BRG_SPAN` | 16.0 mm | Distance between bearing inner faces (min) |
| `SHAFT_OD` | **2.80 mm** | As measured — verify shank |

Derived (set as formulas if your CAD allows):

- `ROTOR_OD` = 2 × (`MAG_FACE_R` + `MAG_T` + `ROTOR_WALL`) = 2 × (22.5 + 2.75 + 3.0) ≈ **56.5 mm**
- Rotor cup axial length = `POCKET_L` + 2.0 ≈ **31.05 mm**
- Tooth root radius ≈ `STATOR_TIP_R` − `TOOTH_H` − `TIP_THICK` (adjust once hub is sized)

---

## Stage 2 — Model the rotor first (45–60 min)

Rotor is driven by magnets + bearings. Get this right, then size the stator to match.

### 2.1 Rotor body sketch (front view, looking along shaft)

1. Draw a circle for **outer OD** = `ROTOR_OD`.
2. Draw a construction circle at radius `MAG_FACE_R` (magnet inner faces).
3. Place **4 magnet pockets** equally spaced (**90°**):
   - Each pocket: rectangle `POCKET_W` × `POCKET_T`
   - Flat of rectangle on the `MAG_FACE_R` circle (apothem/flat facing center)
   - Circumferential centers every 90°
4. Between pockets, leave generous plastic (with only 4 magnets this is easy — do not force magnets edge-to-edge).
5. Extrude rotor cup axial length = `POCKET_L` + **2.0 mm** (1 mm retention lip each end).

### 2.2 Magnet retention

1. At each axial end of every pocket, add a **0.5 mm** radial inward lip (covers ~0.4–0.5 mm of magnet edge).
2. Optional: 0.3 × 0.3 mm glue groove along pocket floor.
3. Chamfer pocket entry 0.2 mm so magnets start easily.

### 2.3 Bearing hub

1. Center hub: outer diameter ~16–18 mm for print strength.
2. Through-bore = `BRG_BORE_PRINT` (9.85 mm).
3. Counterbore or seat two bearings:
   - Bearing 1: flush with rotor **closed end** (or 0.5 mm inside)
   - Bearing 2: spaced so inner faces are ≥ `BRG_SPAN` apart
4. Add 0.2 mm × 45° chamfer on bore entries.
5. Leave a thin wall between bearings or a printed spacer tube (ID > screw head clearance if needed — your shaft is M3 through both IDs).

### 2.4 Rotor print features

- 3–4 × Ø3.2 mm vent/balance holes in the back plate (optional).
- Flat on outer rim or engraved “N” next to pole 1 for magnet install polarity.
- Label alternating poles N/S in notes (not required on model).

**Checkpoint:** Save as `rotor_v1`. Mentally seat a magnet: 28.82×9.25×2.75 should click in with light press + epoxy later.

---

## Stage 3 — Model the stator (60–90 min)

### 3.1 Place the air-gap circle

1. Construction circle radius = `STATOR_TIP_R` (21 mm).
2. Construction circle for bearing hub as needed.

### 3.2 One tooth (then pattern ×3)

Sketch one tooth about the +X axis:

1. **Stem:** width `TOOTH_STEM_W` (8.0 mm), radial length `TOOTH_H` (10 mm).
2. **Tip shoe:** add `TIP_OVERHANG` (1.5 mm) each side of stem; thickness `TIP_THICK` (1.0 mm).
3. Outer tip arc/face sits on `STATOR_TIP_R`.
4. Fillet stem-to-yoke junctions ≥ 0.8 mm.
5. Slight 15–20° undercut under the lips so wire seats behind the shoe.

Extrude tooth axial = `STATOR_STACK` (31 mm).

Circular pattern **3** instances (**120°**).

### 3.3 Inner yoke / hub

1. Join all teeth to a central ring.
2. Target **slot opening** (gap between adjacent tip shoes) ≥ **8 mm** — big gaps make winding much easier.
3. Bore through hub = `BRG_BORE_PRINT`.
4. Seat bearings per Architecture A or B (see Stage 4).

**Recommended simple architecture for hand assembly:**

- **Stator** = 3 teeth + yoke; mounts on a base.
- **Rotor** = cup with 4 magnets + bearings; spins on M3 shaft.

| Architecture | Pros | Cons |
|--------------|------|------|
| **A. Rotor carries both bearings** (stator fixed on base) | Easiest CAD/print | Need a sturdy base + concentric boss |
| **B. Both rotor and stator have bearings on shared M3 shaft** | Classic outrunner feel | Tighter tolerance stack |

**If unsure, use Architecture A** for first print.

### 3.4 Winding access

- Fillet slot bottoms.
- Optional shallow spool flanges at both axial ends of each tooth (0.5–0.8 mm) so turns do not walk off during winding.

**Checkpoint:** Only **3 coils** to wind. Aim ~40 turns of 24 AWG per tooth.

---

## Stage 4 — Shaft, base, and fasteners (30 min)

### Architecture A (recommended first print)

1. **Base / stator mount**
   - Flat plate with a raised **concentric boss** that mates to stator center bore (light press or M3 clamps).
   - Stator tooth OD must clear rotor ID with `AIR_GAP` when assembled.
2. **Shaft**
   - M3 socket head screw, length ~30–40 mm (check your kit).
   - Stack: screw head → washer → rotor bearing(s) → (optional spacer) → nut (or second nut as lock).
3. Ensure screw length: head outside rotor + stack width + nut engagement (≥ 3–4 mm of thread).

### Architecture B

1. M3 screw through: rotor bearing → spacer → stator bearing → spacer → nut.
2. Model printed spacers with ID 3.2 mm, OD 8–9 mm, lengths to set bearing preload lightly (finger snug, not crushed seals).

---

## Stage 5 — Assembly check in CAD (20 min)

Create an assembly (or multi-body) and verify:

1. [ ] 8 magnets seated; faces at `MAG_FACE_R`
2. [ ] Stator tips at `STATOR_TIP_R`
3. [ ] Radial gap = 1.0 mm all around (section view)
4. [ ] No rotor–stator collision through full 360° spin
5. [ ] Bearings sit fully in seats (4 mm depth)
6. [ ] M3 screw clears all IDs
7. [ ] Coil envelope (stem + windings ≈ +1.2 mm radial build) does not hit magnets

Export a **section PDF or screenshot** of the gap for your notes.

---

## Stage 6 — Print prep (15 min)

### Bodies → STL

| File | Orientation on bed | Notes |
|------|--------------------|-------|
| `rotor.stl` | Back plate flat on bed (cup open up) | Best magnet pocket accuracy |
| `stator.stl` | Teeth in XY plane if possible; else hub flat | Prefer strong tooth layer orientation |
| `base.stl` | Flat on bed | |

### Slice settings (starting point)

- Layer: 0.2 mm
- Walls: ≥ 3
- Infill: 40–60% gyro/cubic for rotor cup
- Bed adhesion: brim on rotor
- No ironing on fit faces

### Fit strategy

1. Print a **bearing bore test ring** (10 mm tall, ID 9.90) before the full motor.
2. Press a 623: should need firm thumb/arbor press. If loose, drop print bore to 9.85. If impossible, ream to 10.00.
3. Print a **single magnet pocket coupon**; confirm 3 mm magnet press-fit.

---

## Stage 7 — Physical build order (after CAD/print)

1. Clean supports; ream bearing bores if needed.
2. Epoxy magnets into rotor **alternating N–S** (mark with paint). Let cure.
3. Press bearings.
4. Hand-wind teeth: **~40 turns** on each of **3** teeth (detail in winding note below).
5. Assemble shaft stack; spin by hand — must be free, no scrape.
6. Connect ESC / servo tester; low throttle only for first spin.

### Quick 3N4P winding note (minimal work)

- Only **3 teeth** → phases **A, B, C** (one coil each).
- Wind all three the **same direction** (e.g. always clockwise looking from tip toward hub), same turn count.
- Bring out 6 ends, then join into 3 phase leads for the ESC (or solder as a star: join one end from each coil together as neutral, other three ends to ESC).
- Polarity: magnets around rotor **N–S–N–S**.
- Photograph each tooth before you move on — easy to lose track mid-wind.

---

## Session checklist (do in order)

| Step | Task | Done |
|------|------|------|
| 0 | Caliper all magnets, bearings, screw | [x] |
| 1 | Enter parameters table in CAD (3N4P) | [ ] |
| 2 | Rotor OD + **4** pockets + retention lips | [ ] |
| 3 | Rotor bearing hub + chamfers | [ ] |
| 4 | Stator one tooth → pattern **×3** | [ ] |
| 5 | Stator yoke + wide slot openings (≥ 8 mm) | [ ] |
| 6 | Base (Arch A) or full shaft stack (Arch B) | [ ] |
| 7 | Assembly section: verify 1.5 mm gap | [ ] |
| 8 | Export STLs + bore/magnet test coupons | [ ] |

---

## When you get stuck

Bring to the next chat session:

1. CAD software name
2. Architecture A or B
3. Screenshot of rotor front sketch and stator tooth sketch
4. Any caliper numbers that differed from nominal

Then we can adjust parameters or review a specific sketch dimension.
