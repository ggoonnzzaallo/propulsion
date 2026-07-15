# Propulsion

Hand-wound, FDM-printed brushless motors and related teardown / benchmarking notes.

## Active work

| Build | Version | Status |
|-------|---------|--------|
| [**3N4P outrunner**](builds/3n4p/) | **V1** | Built & tested — **failed to spin** (BEMF too low) — [Onshape CAD](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) |
| [**3N4P outrunner**](builds/3n4p/) | **V2** | CAD in progress — tighter gap, windability & routing refinements; more turns still planned — [Onshape CAD](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e) |

Also: [**benchmarking**](benchmarking/) — tear-downs and reference motors (add photos here).

## Simulator

`src/bldc_sim/` — interactive Streamlit app: slide turns / wire gauge / air gap / geometry and see live BEMF, torque–speed, copper loss, and slot-fill predictions for the air-core 3N4P, with the governing equations shown alongside each result. Presets match V1 (as built) and the V2 draft.

## Local Setup

Requires [uv](https://docs.astral.sh/uv/). From the repo root:

```bash
uv sync                                        # create .venv and install dependencies
uv run streamlit run src/bldc_sim/app.py       # launch the simulator in your browser
uv run pytest                                  # run the model sanity tests
```

## Repo layout

```
propulsion/
├── README.md
├── builds/
│   └── 3n4p/                 ← current motor family
│       ├── README.md         ← topology, hardware, CAD links
│       ├── v1/               ← first print / wind / test
│       └── v2/               ← next iteration plan
├── benchmarking/             ← commercial / reference motor tear-downs
└── docs/                     ← shared CAD & assembly how-tos (legacy + shared)
```

## Quick links

- [3N4P build family](builds/3n4p/README.md)
- [V1 test & troubleshooting log](builds/3n4p/v1/README.md)
- [V2 plan](builds/3n4p/v2/README.md)
- [Benchmarking](benchmarking/README.md)
- Shared guides: [`docs/`](docs/)
