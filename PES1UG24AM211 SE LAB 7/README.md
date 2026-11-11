# SE LAB 7 – Fuzz Testing for Input Validation Bugs

**Student:** Purvik V  
**SRN:** PES1UG24AM211  
**Source assignment:** [L6_L7_29_thermostat_control](https://github.com/SETAPESU26/L6_L7_29_thermostat_control)

## Objective
Use Hypothesis property-based testing to discover invalid and edge-case inputs in a smart thermostat controller, then improve input validation and re-run the test suite.

## Files
- `thermostat_control.py` – corrected thermostat implementation
- `test_thermostat_control.py` – pytest and Hypothesis tests
- `requirements.txt` – test dependencies
- `starter/` – original buggy application and starter test file
- `REPORT.md` – experiment report and results
- `screenshots/` – screenshot folder and naming guide

The formatted PDF report has been generated locally. It still needs to be added to this repository along with the screenshots.

## Setup
```powershell
python -m pip install -r requirements.txt
```

## Run
From this directory:
```powershell
python thermostat_control.py
python -m pytest -v test_thermostat_control.py
```

## Test result
The local test run collected **29 tests** and reported **29 passed in 6.67 seconds**.

## Screenshots to include
See [screenshots/README.md](screenshots/README.md) for the exact filenames and order. Use the genuine screenshots captured from the local runs; do not fabricate terminal output.