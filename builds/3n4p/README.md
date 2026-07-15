# Build family: 3N4P outrunner

Simplest 3-phase DIY outrunner we chose for hand winding: **3 stator teeth, 4 magnet poles**.

## Why 3N4P

- One coil per phase → least winding work  
- Valid for hobby sensorless ESCs (unlike 5-slot ideas)  
- Plastic / air-core stator on v1 for printability  

## Versions

| Version | Status | Summary |
|---------|--------|---------|
| [**V1**](v1/) | Tested — failed | ~40 turns 24 AWG; ESC jerked, no run; BEMF ~mV |
| [**V2**](v2/) | Planned | Raise BEMF (more turns / thinner wire); optional tighter gap |

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
