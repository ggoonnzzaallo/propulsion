# V3 — scoped (not built yet)

Goal: **run continuously for 5 minutes** on the same sensorless ESC, without hand-start drama or V2’s noise / early shutdown.

Keep **3N4P** (3 teeth, 4 magnets), radial-flux outrunner, Architecture A. CAD will change; topology and magnet/bearing hardware stay the same.

## What V2 taught us

| Symptom | Likely cause | V3 fix |
|---------|--------------|--------|
| Loud, wobbly | Loose M3 screw in bearings | Machined **Ø3.00 mm** steel shaft |
| Hand-start, low speed only | Weak flux (plastic core) | Steel tooth laminations + rotor back-iron |
| Hot coils, &lt;1 min stop | Many turns / high I²R for weak flux | More flux → fewer turns, cooler run |

## Scope

### Metal — all via [JLCCNC](https://jlccnc.com/)

| Part | Spec (starting point) | Process |
|------|----------------------|---------|
| Stator tooth laminations | Cold-rolled steel, **0.5 mm**, ~40–42 pcs to ~31 mm stack | Sheet laser |
| Rotor back-iron ring | Magnetic steel (e.g. **45#**), **~2.0–2.5 mm** radial wall, axial length ≈ magnet (~29–31 mm) | CNC turn/mill |
| Shaft | **Ø3.00 mm** steel, bearing shoulders / retention as needed | CNC turn |

Magnets sit against the **ID of the steel ring** (thin glue OK; no thick plastic wall between magnet and steel). Printed rotor parts only locate magnets and hold bearings.

### Printed — PLA for V3

Keep **PLA** on the P1S for V3 carriers (stator hub/shell, rotor cage, base). Switch to **PETG** after V3 if heat / toughness needs it.

- Stator: printed hub/shell clamps the lam stack (alignment pins/bolts); wire routing from V2 carried forward
- Rotor: printed cage around / with the steel ring — magnets touch steel
- Base: shaft fixed, same overall layout as V2

### Insulation & winding

- **Kapton tape** on tooth faces / tips / corners before winding — wire must not sit on bare steel
- No brush epoxy required for V3 (optional later)
- Do **not** put Kapton between laminations (kills flux); sheets stack steel-on-steel, held by the printed hub
- First wind: moderate turns (e.g. ~60–80 of 24–26 AWG), then tune from BEMF — fewer than V2 once iron is in

### Bench gates before “success”

1. Hand-spin **line–line BEMF ≥ ~0.5 V** (aim nearer **1 V**) on a strong flick — same threshold family as the simulator / hobby ESC
2. Sensorless start without a flick (stretch; hand-start OK for first runs if BEMF is healthy)
3. **5 minutes continuous** at a logged low–medium throttle; coils warm OK, no ESC dropout, no melt

## CAD work (new Onshape doc)

Fork from V2 geometry; keep radii / magnet pockets / bearing class. Expected changes:

- Stator body → **lam stack outline** + printable hub (clearance for Kapton + winding)
- Rotor → **steel ring ID/OD** + printed magnet retention (magnets on steel ID)
- Base / shaft stack for true **Ø3.00** shaft and bearing span
- Air gap honest ~1.0 mm once shaft play is gone

CAD link: _TBD_

## Out of scope

- New slot/pole count
- True silicon / electrical steel (JLCCNC CRS / 45# is the compromise)
- Hall sensors
- PETG switch (post-V3)

## Media

_None yet — add photos/videos after first print / metal parts land._
