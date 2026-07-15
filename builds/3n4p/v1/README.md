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

## Photos

| File | Caption |
|------|---------|
| [photos/01-parts-layout.jpg](photos/01-parts-layout.jpg) | Printed parts laid out (stator, base, rotor) |
| [photos/02-rotor-magnets.jpg](photos/02-rotor-magnets.jpg) | Rotor cup with 4 bar magnets seated |
| [photos/03-rotor-magnets-alt.jpg](photos/03-rotor-magnets-alt.jpg) | Rotor magnets, alternate angle |
| [photos/04-stator-first-winding.jpg](photos/04-stator-first-winding.jpg) | First tooth wound |
| [photos/05-stator-windings-complete.jpg](photos/05-stator-windings-complete.jpg) | All three coils wound |
| [photos/06-stator-windings-alt.jpg](photos/06-stator-windings-alt.jpg) | Fully wound stator, alternate close-up |
| [photos/07-stator-phase-leads.jpg](photos/07-stator-phase-leads.jpg) | Phase leads leaving the stator |
| [photos/08-stator-on-base.jpg](photos/08-stator-on-base.jpg) | Wound stator on printed base |
| [photos/09-wired-assembly-face.jpg](photos/09-wired-assembly-face.jpg) | Assembled outrunner, face view + bullets |
| [photos/10-wired-assembly-side.jpg](photos/10-wired-assembly-side.jpg) | Assembled motor, side profile |
| [photos/11-phase-bullet-connectors.jpg](photos/11-phase-bullet-connectors.jpg) | Phase wires / bullet connectors |
| [photos/12-wired-assembly-handheld.jpg](photos/12-wired-assembly-handheld.jpg) | Handheld assembled motor |
| [photos/13-esc-bench-test.jpg](photos/13-esc-bench-test.jpg) | Bench hookup: ESC + servo tester |

## Videos

Compressed from iPhone `.MOV` originals (GitHub-friendly sizes):

| File | Notes |
|------|--------|
| [videos/01-hand-spin.mp4](videos/01-hand-spin.mp4) | Hand-spin / freeness check |
| [videos/02-esc-attempt.mp4](videos/02-esc-attempt.mp4) | ESC powered attempt (jerk / no run) |
| [videos/03-esc-spin-retry.mp4](videos/03-esc-spin-retry.mp4) | Follow-up ESC / assist attempt |

```
v1/
├── README.md
├── photos/
└── videos/
```
