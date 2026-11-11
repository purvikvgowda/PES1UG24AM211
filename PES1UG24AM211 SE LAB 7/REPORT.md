# SE Lab 7 – Fuzz Testing for Input Validation Bugs

**Student:** Purvik V  
**SRN:** PES1UG24AM211  
**Experiment:** Fuzz testing of a Smart Thermostat Controller  
**Source assignment:** [L6_L7_29_thermostat_control](https://github.com/SETAPESU26/L6_L7_29_thermostat_control)

## 1. Objective

To explore fuzz testing and input validation by testing a Smart Thermostat Controller's input-processing functions, identifying failures caused by invalid inputs, applying validation in the corrected implementation, and verifying the behaviour using Hypothesis and pytest.

## 2. Functions tested

1. `parse_setpoint()` – parses a temperature setpoint expressed in Celsius or Fahrenheit.
2. `average_temperature()` – calculates the average of comma-separated sensor readings.
3. `schedule_slot()` – interprets a time in HH:MM format and labels it as a night or day slot.

## 3. Tools and requirements

- Python 3.15.2
- pytest 9.2.0
- Hypothesis 6.170.15
- Windows PowerShell

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the corrected application and tests from this folder:

```powershell
python thermostat_control.py
python -m pytest -v test_thermostat_control.py
```

## 4. Original application – bugs identified

The original starter program did not validate all user inputs before attempting to convert or process them.

### 4.1 Invalid temperature setpoint

- Input: `abc`
- Observed result: `ValueError: could not convert string to float: 'ab'`
- Cause: `parse_setpoint()` attempted a numeric conversion without validating the input first.

### 4.2 Empty sensor reading

- Input: `20.5,,22.5`
- Observed result: `ValueError: could not convert string to float: ''`
- Cause: Splitting the CSV string produced an empty element, which was passed to `float()`.

### 4.3 Invalid time accepted

- Input: `25:70`
- Observed result: The application returned `day 70`.
- Cause: `schedule_slot()` did not enforce the valid hour range (00–23) and minute range (00–59).

## 5. Corrected application – successful execution

The corrected application was executed with these valid inputs:

| Input | Value |
|---|---|
| Setpoint | `21.5C` |
| Sensor readings | `20.5,21,22.5` |
| Time | `07:30` |

Observed output:

- Setpoint in Celsius: `21.5`
- Average Temperature: `21.333333333333332`
- Schedule Slot: `day 30`

## 6. Hypothesis fuzz testing

The test suite used Hypothesis-generated inputs and explicit invalid-input cases to exercise all three functions. The tests checked controlled validation, valid conversions and calculations, malformed inputs, and schedule boundary cases.

Coverage included:
- Setpoint parsing: arbitrary text, `None`, invalid units and formats, Celsius round-trip, and Fahrenheit conversion.
- Average calculation: arbitrary text, `None`, empty readings, malformed CSV entries, and comparison with Python's mean calculation.
- Schedule parsing: arbitrary text, `None`, malformed time strings, out-of-range hour/minute, and night/day boundary checks.

### Test result

Command:

```powershell
python -m pytest -v test_thermostat_control.py
```

| Result | Value |
|---|---:|
| Tests collected | 29 |
| Tests passed | 29 |
| Tests failed | 0 |
| Execution time | 6.67 seconds |

**Outcome: 29 passed in 6.67s.**

## 7. Conclusion

The original program demonstrated input-validation weaknesses in temperature parsing, CSV sensor-reading processing, and time validation. The corrected implementation executed successfully with valid sample inputs. The pytest run collected and passed all 29 tests, providing evidence that the implemented validation and expected behaviours passed the test suite.

## 8. Submission contents

- `thermostat_control.py` – corrected application
- `test_thermostat_control.py` – pytest and Hypothesis test suite
- `requirements.txt` – dependencies
- `starter/` – original starter implementation and starter test file
- `SE_LAB_7_Report.pdf` – formatted report with screenshots (add from the local computer)
- `screenshots/` – original bug demonstrations, corrected execution, and test result screenshots (add from the local computer)
