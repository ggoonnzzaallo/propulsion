# Onshape — start here (3N4P)

Software: **Onshape**. Units: **mm**. Topology: **3 slots / 4 poles**.

**V1 CAD (built & tested):** [Onshape document](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679)  
**V2 CAD (in progress):** [Onshape document](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e)  
Version notes: [`../builds/3n4p/v1/`](../builds/3n4p/v1/) · [`../builds/3n4p/v2/`](../builds/3n4p/v2/)

---

## Session 1 — Variable Studio (do this first)

1. Go to [onshape.com](https://cad.onshape.com) → **Create** → **Document** → name it `bldc_3n4p` (or open the V1 link above).
2. In the document, click the **+** tab (bottom) → **Variable Studio** → name it `motor_vars`.
3. Add these variables (type **Length** unless noted). Expression = the number; units mm.

| Name | Expression |
|------|------------|
| `AIR_GAP` | `1.5 mm` |
| `STATOR_TIP_R` | `21 mm` |
| `MAG_FACE_R` | `22.5 mm` |
| `MAG_L` | `28.82 mm` |
| `MAG_W` | `9.25 mm` |
| `MAG_T` | `2.75 mm` |
| `POCKET_L` | `29.05 mm` |
| `POCKET_W` | `9.4 mm` |
| `POCKET_T` | `2.85 mm` |
| `ROTOR_WALL` | `3 mm` |
| `ROTOR_OD` | `56.5 mm` |
| `BRG_BORE_PRINT` | `9.85 mm` |
| `BRG_W` | `3.97 mm` |
| `BRG_SPAN` | `16 mm` |
| `STATOR_STACK` | `31 mm` |
| `TOOTH_STEM_W` | `8 mm` |
| `TOOTH_H` | `10 mm` |
| `TIP_OVERHANG` | `1.5 mm` |
| `TIP_THICK` | `1 mm` |

4. Optional Number vars: `N_POLES` = `4`, `N_SLOTS` = `3`.
5. Open (or create) a **Part Studio** named `rotor`.
6. In that Part Studio: **Insert** → **Variable Studio** → select `motor_vars` (so `#ROTOR_OD` etc. resolve).

In Onshape sketches/features, reference vars with a leading `#`, e.g. `#ROTOR_OD`.

**Checkpoint:** Variables panel shows the list. Do not sketch until this is done.

---

## Session 2 — Rotor sketch (front view)

Still in Part Studio `rotor`:

1. Select the **Top** plane → **Sketch**.
2. **Circle** centered on origin:
   - Diameter = `#ROTOR_OD` (or radius `28.25 mm`). This is the rotor outer wall.
3. **Construction circle** (toggle Construction) centered on origin:
   - Radius = `#MAG_FACE_R` (`22.5 mm`). Magnet inner faces sit on this.
4. Draw **one** magnet pocket as a rectangle:
   - Width (tangential) = `#POCKET_W` (`9.4 mm`)
   - Depth (radial, outward from the construction circle) = `#POCKET_T` (`2.85 mm`)
   - Place it on the **+X** side: inner flat of the rectangle should lie on the `#MAG_FACE_R` circle (flat facing the center).
5. Tip: sketch a horizontal construction line from origin along +X; use **Midpoint** on the inner flat so the pocket is centered on +X.
6. **Circular pattern** the rectangle (pocket entities only) about the origin:
   - Instance count = **4**
   - Angle = **360°**
7. Between pockets you should see open space — good. Do **not** connect magnets edge-to-edge.
8. Optional: construction circle diameter `#BRG_BORE_PRINT` for the bearing.
9. Green check → rename sketch `rotor_front`.

**Do not extrude yet.** Reply “sketch done” (screenshot helps) → Session 3 is extrude + lips + bearing bore.

### How the pocket should look

```
        outer OD circle
     _____________________
    /    [mag]   [mag]    \     4 pockets at 90°
   |  flat faces inward    |
   |         · origin      |
   |  [mag]         [mag]  |
    \_____________________/
         ↑
   MAG_FACE_R = 22.5 mm to inner flats
```

Each pocket box: **9.4 mm wide × 2.85 mm deep** (deep = radially outward).
