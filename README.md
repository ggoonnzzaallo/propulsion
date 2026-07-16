# Propulsion

DIY **3N4P** plastic-core BLDC outrunner — build logs, BOM, simulator, and one commercial tear-down for reference.

## Builds

| | Result | Log |
|--|--------|-----|
| **V1** | Failed (BEMF too low) | [builds/3n4p/v1/](builds/3n4p/v1/) |
| **V2** | **Runs** | [builds/3n4p/v2/](builds/3n4p/v2/) |

**CAD:** [V1 Onshape](https://cad.onshape.com/documents/c3a46516d37b902d82586f2e/w/ed344aed172445edb6c630d8/e/2b879cec032d2310868e3323?renderMode=0&uiState=6a57b19a1ee05c228a657679) · [V2 Onshape](https://cad.onshape.com/documents/c89f2c87853c9f2774f38798/w/97a941b73ea3b6d03a2aeefd/e/ee342bf624cf2c4ee2937c15?renderMode=0&uiState=6a57b1c4ce1bb754973f165e)

## Docs

- [BOM](docs/bom.md) — Amazon parts, qty per motor
- [Assembly](docs/assembly-magnets-windings.md) — magnets, windings, ESC hookup
- [CAD guide](docs/cad-build-guide.md) — parameters & print notes
- [Simulator](docs/simulator.md) — `bldc_sim` Streamlit app
- [DYS D2830 tear-down](benchmarking/dys-d2830-1000kv/) — reference motor

## Simulator

```bash
uv sync
uv run streamlit run src/bldc_sim/app.py
```
