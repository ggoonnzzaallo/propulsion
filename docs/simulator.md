# `bldc_sim` — analytical motor simulator

Streamlit app + Python models for exploring **air-core 3N4P** design knobs before (or alongside) the next print/rewind.

This is a **lumped-parameter** tool — useful for order-of-magnitude BEMF, fill, and torque–speed trends. It is **not** FEA.

## Run

From the repo root ([uv](https://docs.astral.sh/uv/) required):

```bash
uv sync
uv run streamlit run src/bldc_sim/app.py
uv run pytest
```

## What it does

- Live predictions: **BEMF**, **torque–speed**, **copper loss**, **slot fill**
- Geometry cross-section sketch of the 3N4P layout
- In-app equation notes (kept in sync with `src/bldc_sim/models/equations.py`)
- Presets aligned with build docs:
  - **3N4P V1 (as built)** — 40 turns, 24 AWG, 1.5 mm gap ([V1 log](../builds/3n4p/v1/))
  - **3N4P V2 (draft)** — more turns, thinner wire, tighter gap ([V2](../builds/3n4p/v2/))

Locked hardware numbers should stay consistent with [`cad-build-guide.md`](cad-build-guide.md) and `src/bldc_sim/presets/n3p4.py`.

## Package layout

```
src/bldc_sim/
├── app.py                 ← Streamlit UI
├── geometry/              ← cross-section figure
├── models/                ← motor, winding, magnetic, equations
└── presets/
    └── n3p4.py            ← V1 / V2 draft MotorParams
tests/
└── test_models.py
```

## Relationship to hardware builds

| Artifact | Role |
|----------|------|
| Onshape V1 / V2 | Physical geometry to print |
| `bldc_sim` | Sanity-check turns/gap/wire before winding V2 |
| V1 BEMF ~mV | Motivates higher-turn presets in the sim |

When CAD gap or turn targets change, update **both** `builds/3n4p/v2/README.md` and the `V2_DRAFT` preset in `presets/n3p4.py`.
