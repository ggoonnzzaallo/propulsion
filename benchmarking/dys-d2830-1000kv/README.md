# Tear-down: DYS D2830 1000KV

**Date:** 2026-07 (photos from iPhone)  
**Source:** Purchased DYS / G-Power **D2830 1000KV** brushless outrunner (Amazon listing PDF below)

Commercial reference motor — torn down to study real outrunner construction vs our DIY [3N4P](../../builds/3n4p/).

## Identity

| Field | Value |
|-------|--------|
| Markings / KV / size | **DYS G-Power**, stickers **D2830 / 1000KV** |
| Topology (counted) | **12N14P** — 12 stator teeth, 14 rare-earth magnets |
| Outrunner / inrunner | **Outrunner** |
| Sensored? | Sensorless (3 phase leads only) |

## Product docs

- [Amazon listing — DYS D2830 1000KV](docs/amazon-listing-dys-d2830-1000kv.pdf)
- [Amazon listing — ESC + servo tester (drive gear used on DIY)](docs/amazon-listing-esc-servo-tester.pdf)

## Measured / observed (hand teardown)

| Feature | Value |
|---------|--------|
| Stator outer diameter | **22.0 mm** |
| Stator stack height | **14.5 mm** |
| Bare wire diameter | **0.22 mm** (~**31–32 AWG**) |
| Magnet size | **4 × 12 × 2 mm** |
| Magnet count | **14** |
| Stator teeth (slots) | **12** |
| Topology | **12N14P** |
| Winding style | **2-strand parallel** — two thin wires wound together per tooth (packs corners tightly) |
| Turns / tooth (estimate) | **~12–15** physical wraps per tooth |

Shaft OD, bearings, and air gap not recorded yet — add if re-measured.

## Photos

| File | Caption |
|------|---------|
| [photos/01-outside-label.jpg](photos/01-outside-label.jpg) | Assembled motor, wraparound DYS G-Power label, RGB phase wires |
| [photos/02-model-stickers.jpg](photos/02-model-stickers.jpg) | D2830 / 1000KV stickers on bell |
| [photos/03-side-profile.jpg](photos/03-side-profile.jpg) | Side profile: shaft both ends, rear circlip, set screw |
| [photos/04-bottom-mount-circlip.jpg](photos/04-bottom-mount-circlip.jpg) | Orange mount base, holes, E-clip over center bearing |
| [photos/05-hub-set-screw.jpg](photos/05-hub-set-screw.jpg) | Hub set screw locking the shaft |
| [photos/06-rotor-bell-label.jpg](photos/06-rotor-bell-label.jpg) | Separated rotor bell with label |
| [photos/07-rotor-magnets-marks.jpg](photos/07-rotor-magnets-marks.jpg) | Rotor interior: magnet ring (some magnets marked) |
| [photos/08-rotor-hub-magnets.jpg](photos/08-rotor-hub-magnets.jpg) | Rotor: magnets + three-spoke hub |
| [photos/09-stator-base-bearing.jpg](photos/09-stator-base-bearing.jpg) | Stator mount plate + bearing + vents |
| [photos/10-stator-windings-wires.jpg](photos/10-stator-windings-wires.jpg) | Stator windings overview + phase leads |
| [photos/11-stator-overview.jpg](photos/11-stator-overview.jpg) | Handheld stator overview |
| [photos/12-stator-laminations.jpg](photos/12-stator-laminations.jpg) | Laminated teeth / slots + copper |
| [photos/13-stator-teeth-macro.jpg](photos/13-stator-teeth-macro.jpg) | Macro: insulated tooth faces + bearing |
| [photos/14-bearing-windings-macro.jpg](photos/14-bearing-windings-macro.jpg) | Macro: copper strands + seated bearing |

## Takeaways for DIY

- **Iron laminated** 12-tooth stator + **14** magnets in a metal bell — much higher flux than our plastic 3N4P V1/V2 core.
- Wire is fine (**~0.22 mm / 31–32 AWG**) with **few wraps** (~12–15) but **2-in-hand** — high copper density without single thick strands.
- Magnets are small **4×12×2 mm** blocks, dense ring packing — not large sparse bars.
- Same class of **sensorless ESC + 3 leads** we use on the DIY motor.
- Dual-end shaft + set screw + circlip is a robust shaft retention pattern vs a single M3 through-stack.
