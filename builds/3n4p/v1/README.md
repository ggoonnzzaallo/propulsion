# 3N4P — V1 (built & tested)

**Status:** Failed first spin. Root cause: **back-EMF too low** for sensorless ESC lock.

Printed plastic stator/rotor/base, wound ~**40 turns/tooth** of **24 AWG**, star-connected (starts = neutral, ends → ESC), magnets **N–S–N–S**.

### CAD (Onshape)

**V1 document:** [BLDC — Onshape](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679)

CAD / assembly process used during V1: [`../../docs/`](../../docs/).

---

## What worked

- Onshape parts assembled and spun freely by hand (when fasteners not over-tight)
- Magnet polarity confirmed N–S–N–S
- Phase resistances similar (~**0.2 Ω** between ESC leads)
- All three coils wound the **same direction**
- Star used **starts** as neutral and **ends** to ESC (as intended)
- ESC armed with normal tones

## Failure mode

Under throttle the rotor **jerked** but never ran continuously.  
A hand flick while the ESC was powered did **not** bring it into sync.

## Troubleshooting tried

| Check | Result |
|-------|--------|
| Loosen fasteners / reduce friction | No change |
| Hand-spin assist while ESC powered | No lock / no run |
| Phase swap (at least one swap; not exhaustive) | Same jerk behavior |
| Confirm starts = neutral, ends → ESC | Confirmed |
| Confirm all winds same direction | Confirmed |
| Multimeter continuity / phase R | ~0.2 Ω, consistent |
| Magnet N–S–N–S | Confirmed |
| Star flip (join the other trio as neutral) | **Not completed** — neutral leads cut too short to repackage easily; lower priority after BEMF result |
| **BEMF test** (ESC disconnected, meter AC on two phases, hard hand spin) | Only **~0.2–1 mV** — had to use **mV** range |

## Conclusion

Electrical hookup and magnets are plausible. The machine is **magnetically too weak** as built:

- Air / plastic core (no iron flux path)
- Modest turns of relatively thick wire
- ~1.5 mm air gap

Sensorless ESCs need far more BEMF than millivolts to commutate after the open-loop kick — hence **jerk, then nothing**.

Phase-order or star mistakes can cause similar symptoms, but the BEMF measurement says **even a correct ESC would struggle**.

## Carry into V2

Do **not** expect V1 hardware to run by more phase swapping alone.  
Raise BEMF first — see [V2 plan](../v2/).

## Photos / exports

Add V1 photos, Onshape export links, or STLs here when available:

```
v1/
├── README.md          ← this file
├── photos/            ← optional
└── exports/           ← optional STL/STEP snapshots
```
