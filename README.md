# Propulsion

DIY BLDC motors — build logs, benchmarking, and an analytical simulator.

## Builds

### [3N4P outrunner](builds/3n4p/)

3 teeth / 4 magnets — fewest coils for a hobby 3-phase ESC. Plastic core through V2; V3 adds steel.

| Version | Result | What changed |
|---------|--------|--------------|
| [V1](builds/3n4p/v1/) | Failed — ESC jerked, never spun | ~40 T / 24 AWG, ~1.5 mm gap; BEMF ~mV |
| [V2](builds/3n4p/v2/) | Spins — hand-start, low speed, noisy, &lt;1 min | Tighter gap, more turns, better routing |
| [V3](builds/3n4p/v3/) | Scoped — goal **5 min continuous** | JLCCNC steel lams + back-iron + Ø3 shaft; PLA prints |

BOM, assembly, and CAD notes live on the [3N4P page](builds/3n4p/).

## Benchmarking

Hobby tear-down + MIT Cheetah–family actuator reference: **[benchmarking/](benchmarking/)**

## Simulator

```bash
uv sync
uv run streamlit run src/bldc_sim/app.py
```

Details: [docs/simulator.md](docs/simulator.md)
