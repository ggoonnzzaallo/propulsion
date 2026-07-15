# Propulsion

Hand-wound, FDM-printed brushless motors, tear-down notes, and an analytical parameter simulator for the air-core **3N4P** outrunner.

## Active work

| Build | Version | Status |
|-------|---------|--------|
| [**3N4P outrunner**](builds/3n4p/) | **V1** | Built & tested — **failed to spin** (BEMF too low) — [Onshape CAD](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) |
| [**3N4P outrunner**](builds/3n4p/) | **V2** | CAD in progress — tighter gap, thinner tips (0.5 mm), windability & routing; more turns still planned — [Onshape CAD](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e) |

Also:
- [**Simulator**](docs/simulator.md) — Streamlit / `bldc_sim` (BEMF, torque–speed, fill, etc.)
- [**Benchmarking**](benchmarking/) — tear-downs ([DYS D2830 1000KV](benchmarking/dys-d2830-1000kv/))

## Simulator (`bldc_sim`)

Python package under `src/bldc_sim/`: lumped-parameter model (not FEA) with a Streamlit UI. Slide turns, wire gauge, air gap, and geometry; compare presets for **V1 as-built** vs **V2 draft**.

Details: [`docs/simulator.md`](docs/simulator.md).

## Local Setup

Requires [uv](https://docs.astral.sh/uv/). From the repo root:

```bash
uv sync                                        # create .venv and install dependencies
uv run streamlit run src/bldc_sim/app.py       # launch the simulator in your browser
uv run pytest                                  # run the model sanity tests
```

Hardware / CAD work does not require the Python env — clone and open the Onshape links + guides under `docs/` and `builds/`.

## Repo layout

```
propulsion/
├── README.md
├── pyproject.toml            ← uv project (bldc-sim)
├── uv.lock
├── src/bldc_sim/             ← analytical simulator + Streamlit app
├── tests/                    ← pytest for models
├── builds/
│   └── 3n4p/                 ← motor family
│       ├── v1/               ← first print / wind / test (failed)
│       └── v2/               ← CAD iteration + BEMF plan
├── benchmarking/             ← commercial / reference tear-downs
└── docs/                     ← CAD, winding, simulator how-tos
```

## Quick links

- [3N4P build family](builds/3n4p/README.md)
- [V1 test & troubleshooting log](builds/3n4p/v1/README.md)
- [V2 CAD changelog & plan](builds/3n4p/v2/README.md)
- [Simulator docs](docs/simulator.md)
- [Benchmarking](benchmarking/README.md)
- Shared CAD/winding guides: [`docs/`](docs/)
