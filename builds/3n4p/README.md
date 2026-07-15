# Build family: 3N4P outrunner

Simplest 3-phase DIY outrunner we chose for hand winding: **3 stator teeth, 4 magnet poles**.

## Why 3N4P

- One coil per phase → least winding work  
- Valid for hobby sensorless ESCs (unlike 5-slot ideas)  
- Plastic / air-core stator on v1 for printability  

## Versions

| Version | Status | Summary |
|---------|--------|---------|
| [**V1**](v1/) | Tested — failed | ~40 turns 24 AWG; ESC jerked, no run; BEMF ~mV — [Onshape CAD](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) |
| [**V2**](v2/) | CAD in progress | Tighter gap (under ~1 mm min), fillets, rotor windows, press chamfer, winding body, base wire routing — [Onshape CAD](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e) |

## Locked hardware (shared across versions unless noted)

| Part | Measured |
|------|----------|
| Magnets | **2.75 × 9.25 × 28.82 mm** — use **4**, N–S–N–S |
| Bearings | ~Ø9.96 × Ø2.99 × 3.97 mm (623-class) |
| Shaft | M3 ~Ø2.80 (prefer true Ø3.00 later) |
| Drive | ~30 A sensorless ESC + servo tester |

## CAD highlights (V1 baseline)

| Param | Value |
|-------|-------|
| Air gap | 1.5 mm |
| Stator tip R | 21.0 mm |
| Magnet face R | 22.5 mm |
| Rotor OD | ~56.5 mm |
| Stator stack | 31 mm |
| Topology | Architecture A (stator on base; bearings in rotor) |

Full tables & Onshape notes live under [`../../docs/`](../../docs/).
