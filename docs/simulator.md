# Simulator

Lumped-parameter **3N4P** model (not FEA). Presets match V1 and V2 in `src/bldc_sim/presets/n3p4.py`.

```bash
uv sync
uv run streamlit run src/bldc_sim/app.py
uv run pytest
```

Shows BEMF, torque–speed, copper loss, and slot fill vs turns / wire / gap.
