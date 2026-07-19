# MIT low-cost modular actuator (Katz 2018)

Reference for where this project wants to go long-term: a **proprioceptive, backdrivable joint actuator** in the MIT Cheetah family — high torque-density BLDC + **low-ratio single-stage planetary**, torque from motor current (no SEA / joint torque sensor).

**Source:** Benjamin G. Katz, *A Low Cost Modular Actuator for Dynamic Robots*, S.M. thesis, MIT MechE, June 2018 (advisor Sangbae Kim).  
PDF: [docs/katz-2018-low-cost-modular-actuator.pdf](docs/katz-2018-low-cost-modular-actuator.pdf)

This design is the cheap modular unit that enabled the Mini Cheetah–class platform (12‑DoF quadruped, including a standing backflip). It follows the same actuation *paradigm* as Cheetah 2/3, but with off-the-shelf drone motor guts and stock gears instead of custom motors.

## Actuator specs (Table 2.2)

| | |
|--|--|
| Mass | **480 g** |
| Envelope | **Ø96 mm × 40 mm** axial |
| Peak torque (output) | **17 N·m** |
| Continuous torque | **6.9 N·m** |
| Max output speed | **40 rad/s** @ 24 V |
| Peak power | **+250 W / −680 W** (regen) |
| Current-control bandwidth | **4.5 kHz** @ 4.5 N·m · **1.5 kHz** @ 17 N·m |
| Output inertia | **0.0023 kg·m²** |
| Backlash | ~**0.005 rad** (0.28°) |
| Cogging / ripple (output) | ~**0.25 N·m** position-dependent |
| Static friction (output) | ~**0.09 N·m** (+ ~0.04 N·m per N·m load) |
| BOM (sub‑50 qty) | **~$300** / actuator |

## Motor + transmission

| | |
|--|--|
| Motor | OTS large-drone outrunner, **≈ T-Motor U8** class (**$60–90**; U8 itself ~3× that) |
| Air-gap diameter | **81 mm** |
| Stack length | **8.2 mm** |
| Pole-pairs | **21** (42 magnets) |
| Motor peak torque | ~**2.8 N·m** class before gearing (Kt drops ~12% at max current) |
| Gear | **6:1** single-stage planetary (stock Misumi planets/sun + KHK ring) |
| Packaging | Planetary packed in stator through-bore; rotor post-machined for sun + encoder magnet |
| Sensing | On-board **AS5047P** magnetic encoder (FOC commutation) |
| Drive | Integrated inverter ~**24 V**, **40 A** peak phase |

## Design principles (why it matters for us)

1. **Proprioceptive force control** — joint torque ≈ gear × Kt × current; no output torque sensor  
2. **Low gear ratio** — backdrivable, impact-tolerant, high mechanical bandwidth (vs high-ratio + SEA)  
3. **Large gap radius / short stack** — maximize torque density of the EM machine  
4. **Cost** — Cheetah 2/3 custom actuators dominate robot cost; this module is **1–2 orders of magnitude cheaper**; whole quadruped BOM &lt; one Cheetah actuator  

Scaled target from Cheetah 3 (Table 2.1): 41 kg robot → ~9.5 kg mini with ~30 N·m joints; this actuator lands at **17 N·m** peak (motor availability limited the exact scale).

## vs our 3N4P DIY

| | Our V1–V3 | Katz modular actuator |
|--|-----------|------------------------|
| Goal today | Learn windings, flux, ESC, run for minutes | Legged proprioceptive joint |
| Machine | 3N4P printed / hybrid steel | High pole-count large-gap outrunner |
| Gearing | Direct (none) | 6:1 planetary |
| Control | Hobby sensorless ESC | FOC current + joint commands |
| Cost class | Tens of $ | ~$300 / joint |

**North star:** keep iterating motor construction (V3 steel, shaft fit, thermal), then move toward a **compact high-torque outrunner + low-ratio gearbox + current-mode drive** in this spirit — not a copy of U8 geometry on day one.

## Citations

- Katz, B. G. (2018). *A Low Cost Modular Actuator for Dynamic Robots*. MIT S.M. thesis.  
- Related paradigm paper: Wensing et al., “Proprioceptive Actuator Design in the MIT Cheetah…,” *IEEE T-RO*, 2017.
