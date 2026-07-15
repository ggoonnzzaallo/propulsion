# Propulsion — 3D-Printed BLDC Outrunner

Hand-wound, FDM-printed **radial-flux outrunner** brushless motor, driven by a hobby **sensorless ESC** and a CCPM servo tester.

This repo documents the design parameters, CAD process (Onshape), assembly, and what we learned from the first hardware spin.

## Goals

- Build the **simplest workable** 3-phase DIY outrunner (fewest coils to wind).
- Use only purchased hobby hardware + printed plastic (no iron laminations on v1).
- Keep geometry **parametric** so air gap, pockets, and stack length track caliper measurements.

## Architecture (locked)

| Item | Choice | Notes |
|------|--------|--------|
| Topology | **3N4P** (3 slots / 4 poles) | One coil per phase — least winding work |
| Layout | Radial-flux **outrunner** | Magnets on the rotating cup; coils on the fixed stator |
| Stator core | **Plastic / air-core** | Easy to print; magnetically weak vs iron |
| Mounting | Architecture A | Stator fixed to base; bearings in rotor; fixed M3 shaft |
| CAD | **Onshape** | Variables drive all critical dimensions |
| Drive | ~30 A sensorless ESC + servo tester | |

We briefly considered 6N8P and 5N6P. **5N6P is not valid** for normal 3-phase ESCs (slot count must be divisible by 3). **3N4P** won for simplicity.

## Hardware (caliper-locked)

| Part | Measured | Qty used |
|------|----------|----------|
| Neodymium bar magnets | **2.75 × 9.25 × 28.82 mm** (T × W × L) | **4** of 12 on hand (N–S–N–S) |
| Bearings | 623-style: **Ø9.96 OD × Ø2.99 ID × 3.97 W** | 2 in rotor hub/tower |
| Shaft | M3 SHCS ~**Ø2.80** (loose in bearing) | Prefer true Ø3.00 rod later |
| Wire | 24 AWG enameled magnet wire | First spin: ~40 turns/tooth |
| Electronics | Hobby sensorless ESC (~30 A) + servo tester | |

### Magnet orientation in CAD

| Axis | Size | Role |
|------|------|------|
| Radial | 2.75 mm | Pocket depth (`MAG_T`) |
| Circumferential | 9.25 mm | Pocket width (`MAG_W`) |
| Axial | 28.82 mm | Stack length (`MAG_L`) |

## Key design numbers

| Parameter | Value |
|-----------|-------|
| Air gap (tooth tip → magnet face) | **1.5 mm** (loose shaft play budget) |
| Stator tip radius | 21.0 mm |
| Magnet face radius | 22.5 mm |
| Rotor OD | ~56.5 mm |
| Stator stack | 31 mm |
| Tooth stem | 8 mm wide (easy winding) |
| Bearing print bore | Ø9.85 mm (press onto ~9.96 OD) |
| Winding axial keep-out | ~5 mm above/below stack (end turns not modeled in CAD) |

Full variable table and sketch steps: [`docs/cad-build-guide.md`](docs/cad-build-guide.md), Onshape walkthrough: [`docs/onshape-session.md`](docs/onshape-session.md).

## Winding & connections

- **3 coils**, same wind direction on every tooth.
- First attempt: ~**40 turns** of 24 AWG per tooth.
- **Star (Wye):** join all **starts** as insulated neutral; send all **ends** to the ESC.
- Magnets around rotor: **N–S–N–S** on the faces toward the stator.

See [`docs/assembly-magnets-windings.md`](docs/assembly-magnets-windings.md).

**Start vs end** means winding time order (first lead vs last lead), not tip vs hub.

## Current status

### Done
- [x] Hardware measured and parameters locked
- [x] Onshape model: rotor (4 pockets + cup), stator (3 T-teeth), base
- [x] Magnets installed N–S–N–S
- [x] Stator wound (~40 T), star-connected
- [x] First electrical attempt with ESC

### First-spin result
ESC arms normally. Under throttle the rotor **jerks** but does not run, including with a hand flick.

Diagnostics:
- Phase resistance ~**0.2 Ω** (pairs similar — continuity OK)
- Star uses **starts** as neutral; winds same direction
- Hand-spin **BEMF** only ~**0.2–1 mV** AC phase-to-phase

**Conclusion:** coupling is too weak for a sensorless ESC. The ESC open-loop-kicks, then never sees enough back-EMF to commutate. This is expected for a plastic-core motor with thick wire and modest turns — not primarily a phase-order bug.

### Next (highest leverage)
1. **Rewind** with many more turns (target **100–150+** / tooth), thinner wire (**28–30 AWG**) if 24 AWG will not fit
2. Optionally reprint with **~1.0 mm** air gap if shaft concentricity improves (true Ø3 shaft)
3. Keep documenting Onshape exports (STEP/STL) in this repo when ready

## Repo layout

```
propulsion/
├── README.md                 ← you are here
└── docs/
    ├── cad-build-guide.md    ← parameters + modeling stages
    ├── onshape-session.md    ← Onshape-specific Session 1–2
    └── assembly-magnets-windings.md
```

CAD lives in Onshape for now; export STLs/STEPs here when versions stabilize.

## Local setup

This is a **hardware / CAD** project (not a Python package).

1. Clone the repo.
2. Open or recreate the Onshape document using variables in `docs/cad-build-guide.md`.
3. Print PETG (preferred) or PLA; verify bearing and magnet pocket fits with coupons first.
4. Assemble per `docs/assembly-magnets-windings.md`.

## Safety

- Neodymium magnets pinch hard — watch bearings and fingers.
- Low coil resistance + ESC can draw large current spikes; use a proper LiPo/bench supply rated for the ESC and start at low throttle.
- Stop immediately if anything scrapes or smells hot.

## License

TBD — add a license before making the repo public if you care about reuse terms.
