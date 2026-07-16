# 3N4P — V2 (built & tested)

**Status:** **Success** — motor runs on sensorless ESC.

Addresses V1’s **too-low back-EMF** with tighter air gap, improved windability/routing, and a higher-turn rewind.

### CAD (Onshape)

**V2 document:** [BLDC V2 — Onshape](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e)

Still **3N4P**, Architecture A, same magnets/bearings family as V1.

---

## What changed vs V1

| Change | Detail |
|--------|--------|
| **Tighter air gap** | Rotor diameter reduced — min magnet↔stator clearance **under ~1 mm** |
| **Thinner tooth tips** | `#TIP_THICK` **1.0 → 0.5 mm** |
| **Tip-corner fillets** | **0.5 mm** fillets on tip corners |
| **Stator fillets** | Easier / safer winding |
| **Rotor visibility cutouts** | See interior when assembled |
| **Stator press chamfer** | Press-fit onto base |
| **Winding body (CAD)** | Keep-out for coil bundle |
| **Base wire routing** | Phase leads + neutral management |
| **Electrical** | More turns + finer wire (vs V1’s ~40 T / 24 AWG) |

V1 failure context: [V1 log](../v1/) — BEMF ~mV, ESC jerk only.

---

## Result

- [x] Motor **runs continuously** on sensorless ESC
- [x] First successful spin documented (see videos)
- [ ] Formal BEMF measurement logged (optional follow-up)

---

## Photos

| File | Caption |
|------|---------|
| [photos/01-3dprinted-parts.jpg](photos/01-3dprinted-parts.jpg) | V2 printed parts: stator, base, rotor |
| [photos/02-3dprinted-parts-alt.jpg](photos/02-3dprinted-parts-alt.jpg) | Printed parts, alternate layout |
| [photos/03-winding-start.jpg](photos/03-winding-start.jpg) | Winding in progress — two coils done |
| [photos/04-winding-progress.jpg](photos/04-winding-progress.jpg) | Two coils wound, spool on bench |
| [photos/05-winding-progress-2.jpg](photos/05-winding-progress-2.jpg) | All three coils wound; leads routed through base |
| [photos/06-winding-progress-3.jpg](photos/06-winding-progress-3.jpg) | Finished stator, all coils wound |
| [photos/07-winding-complete.jpg](photos/07-winding-complete.jpg) | Wound stator with center shaft installed |
| [photos/08-assembly-rotor-on-stator.jpg](photos/08-assembly-rotor-on-stator.jpg) | Stator in housing, phase leads to bullets |
| [photos/09-assembly-wired.jpg](photos/09-assembly-wired.jpg) | Top frame installed, coils visible |
| [photos/10-assembly-on-base.jpg](photos/10-assembly-on-base.jpg) | Near-complete assembly, handheld |
| [photos/11-wire-routing.jpg](photos/11-wire-routing.jpg) | Backplate: star neutral joint + routed leads |
| [photos/12-final-assembly.jpg](photos/12-final-assembly.jpg) | Completed motor on bench, ready to drive |
| [photos/13-v1-next-to-v2.jpg](photos/13-v1-next-to-v2.jpg) | V1 vs V2 side-by-side |
| [photos/14-v1-next-to-v2-alt.jpg](photos/14-v1-next-to-v2-alt.jpg) | V1 vs V2 top-down comparison |
| [photos/15-esc-test-running.jpg](photos/15-esc-test-running.jpg) | Test setup — motor + power connector |
| [photos/16-esc-test-running-alt.jpg](photos/16-esc-test-running-alt.jpg) | Motor wired to 30 A ESC on bench |

## Videos

Compressed from iPhone `.MOV` originals:

| File | Notes |
|------|--------|
| [videos/01-first-run.mp4](videos/01-first-run.mp4) | **First successful run** |
| [videos/02-longest-run.mp4](videos/02-longest-run.mp4) | Longest continuous run |

```
v2/
├── README.md
├── photos/
└── videos/
```
