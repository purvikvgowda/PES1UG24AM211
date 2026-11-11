# SE LAB 7 – Fuzz Testing for Input Validation Bugs

**Student:** PURVIK V  
**SRN:** PES1UG24AM211  
**Source assignment:** [L6_L7_29_thermostat_control](https://github.com/SETAPESU26/L6_L7_29_thermostat_control)

## Objective
Use Hypothesis property-based testing to discover invalid and edge-case inputs in a smart thermostat controller, then improve input validation and re-run the test suite.

## Files
- `thermostat_control.py` – thermostat functions (starter and hardened implementation documented in commits)
- `test_thermostat_control.py` – pytest and Hypothesis tests
- `requirements.txt` – test dependencies
- `screenshots/` – add genuine screenshots from the local runs
- `SE_LAB_7_Report.pdf` – add the screenshot report after completing the lab

## Setup
```powershell
python -m pip install -r requirements.txt
```

## Run
From this directory:
```powershell
python thermostat_control.py
python -m pytest -q
```

## Test strategy
Hypothesis generates text, numeric, boolean, list, and boundary values for:
- `parse_setpoint`
- `average_temperature`
- `schedule_slot`

The property tests check controlled validation: valid inputs return documented results, while invalid input is rejected with a clear `ValueError` or `TypeError`, rather than an incidental exception.

## Screenshots
Capture the original failing test run and the final passing test run on your machine and place them in `screenshots/`. Do not use fabricated terminal output.
