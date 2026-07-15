# 3N4P — Magnets, Windings, Connections

Parts in hand: printed rotor / stator / base, 4 magnets (of 12), 24 AWG, 623 bearings, M3 hardware, ESC + servo tester.

---

## 1. Permanent magnets (rotor)

### Polarity pattern
Around the rotor, **alternate**:

```
        N
    S       S
        N
```

Viewed from above (looking into the cup): go around in order **N → S → N → S**.

Every magnet’s **inner face** (toward the stator) is what matters. Neighboring magnets must show **opposite** poles to the center.

### How to tell N from S
1. Take two magnets. Faces that **attract** are opposite poles; faces that **repel** are the same pole.
2. Pick one face as **N** and mark it with a permanent marker (dot or “N”).
3. Mark all magnets the same way before gluing.
4. Optional: a compass — the needle’s **N** end points toward a magnet’s **S** face (easy to mix up; marker + attract/repel is safer).

### Install
1. Clean pockets; dry-fit each magnet (should be snug).
2. Put a thin layer of **epoxy** (or CA + backing epoxy) in a pocket.
3. Press magnet in: **marked face toward center** (toward stator), following N-S-N-S.
4. Wipe squeeze-out. Magnet face should sit near the inner cavity wall, not tilted.
5. Do opposite magnet next (helps balance pull), then the last two.
6. Cure fully before spinning (per epoxy instructions).

**Do not** put all N facing in — the motor will not run.

---

## 2. Bearings (rotor)

1. Press both **623-2RS** into the rotor bearing tower (ID on the M3 shaft later).
2. Inner races must spin freely on the shaft; outer races locked in the print.
3. If tower is short: one bearing in rotor floor, second in a tall hub — span them as far apart as the design allows (≥ ~16 mm ideal).

---

## 3. Wind the stator (3 coils)

You wind **one coil per tooth** = phases **A, B, C**.

### Targets
| Item | Value |
|------|--------|
| Wire | 24 AWG enameled |
| Turns per tooth | **~40** (30–40 OK) |
| Direction | **Same on all three teeth** |
| Leads | Leave **~100–120 mm** free at start and end of each coil |

### Direction (pick one and never change it)
Looking at a tooth from **outside** (tip toward you, hub away):

- Wind **clockwise** on tooth A, B, and C — all identical.

Mark the start of each coil with tape: `A-start`, `B-start`, `C-start`. Finish leads: `A-end`, `B-end`, `C-end`.

### How to wind one tooth
1. Leave a long start lead; tape it temporarily to the hub.
2. Feed wire through the gap beside the tooth, under the **tip shoe**, around the stem.
3. Each pass around the stem = 1 turn. Keep layers neat; fill left/right of the stem evenly.
4. Stay **under the shoes** — do not pile wire past the tip toward where magnets will be.
5. Count to **40**. Leave a long finish lead.
6. Snug end turns with a tiny drop of CA or hot glue on the coil (not on the enamel you’ll later strip).

Repeat for the other two teeth. Same turn count and same direction.

### Order around the stator
Going clockwise around the hub, label teeth:

```
        A
     C     B
```

(Any labeling is fine if you stay consistent when connecting.)

---

## 4. Connections (to the ESC)

Hobby **sensorless ESC** expects **3 phase wires**. Use a **star (Wye)** connection — simplest for a first motor.

### Star (recommended)
1. Strip enamel off the last ~10 mm of each lead (sandpaper, flame carefully then sand, or enamel scraper).
2. Twist together **A-start + B-start + C-start** → this is **neutral**.
3. Solder and **insulate** (heat-shrink). Neutral does **not** go to the ESC.
4. The three finishes go to the ESC:
   - `A-end` → ESC phase 1  
   - `B-end` → ESC phase 2  
   - `C-end` → ESC phase 3  

ESC phase order is arbitrary at first. If it doesn’t spin, swap any **two** phase wires.

```
    A-end ──●──────────────── ESC wire 1
            │
    B-end ──●──────────────── ESC wire 2
            │
    C-end ──●──────────────── ESC wire 3

    A-start ─┬─ B-start ─┬─ C-start   → soldered & insulated (neutral)
```

### If start/end got confused
For each coil you only need two ends. Star = **join one end from each coil**; other three ends → ESC. If direction was consistent, it will run (or run after swapping two ESC leads).

### Delta (optional, not needed now)
Join A-end→B-start, B-end→C-start, C-end→A-start; those three joints → ESC. Higher current / “faster” feel. Use star first.

---

## 5. Mechanical assembly order

1. Magnets epoxied & cured in rotor; bearings pressed.
2. Stator wound & connected (leads sleeved so they can’t rub the rotor).
3. Stator fixed to base (**screws / flat**) with **~5 mm** winding clearance under the coils.
4. M3 shaft fixed in base, pointing up through the hub.
5. Drop rotor on so bearings slide onto M3; magnets surround stator.
6. Secure with washer + nut — snug, **not** crushing bearing seals.
7. Hand-spin: must turn freely, no scrape. Check air gap.

---

## 6. First electrical spin

1. ESC phase wires → three star finishes; ESC power → battery (correct polarity).
2. Signal → servo tester; start **low**.
3. If silent: give rotor a **gentle flick** (sensorless + weak air-core often needs help).
4. If it growls / vibrates hard: swap **any two** phase leads.
5. If it scrapes: stop immediately — fix mechanical gap before more throttle.

---

## Quick checklist

- [ ] Magnets **N-S-N-S** facing inward  
- [ ] 3 coils, same direction, ~40 turns each  
- [ ] Star: three starts tied & insulated; three ends → ESC  
- [ ] Stator locked to base; windings clear of plate & rotor  
- [ ] Bearings on fixed M3; rotor spins by hand free  
- [ ] Low throttle + flick; swap two phases if needed  
