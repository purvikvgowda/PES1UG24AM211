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
- `SE_LAB_7_Report.pdf` – formatted report (PDF)
- `screenshots/` – genuine screenshots from local runs

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
Place the genuine terminal screenshots in a `screenshots` folder:
1. `01_parse_setpoint_error.png`
2. `02_average_temperature_error.png`
3. `03_schedule_slot_error.png`
4. `04_fixed_application.png`
5. `05_hypothesis_tests.png`

Do not use fabricated terminal output.