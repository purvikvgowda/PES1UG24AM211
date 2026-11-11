import math

import pytest
from hypothesis import given, strategies as st

from thermostat_control import (
    average_temperature,
    parse_setpoint,
    schedule_slot,
)


@given(st.text())
def test_parse_setpoint_never_leaks_unexpected_exceptions(value):
    try:
        result = parse_setpoint(value)
    except ValueError:
        return
    assert isinstance(result, float)
    assert math.isfinite(result)


@given(st.none())
def test_parse_setpoint_rejects_none(value):
    with pytest.raises(TypeError):
        parse_setpoint(value)


@given(st.text())
def test_average_temperature_never_leaks_unexpected_exceptions(value):
    try:
        result = average_temperature(value)
    except ValueError:
        return
    assert isinstance(result, float)
    assert math.isfinite(result)


@given(st.none())
def test_average_temperature_rejects_none(value):
    with pytest.raises(TypeError):
        average_temperature(value)


@given(st.text())
def test_schedule_slot_never_leaks_unexpected_exceptions(value):
    try:
        result = schedule_slot(value)
    except ValueError:
        return
    assert result.startswith(("night ", "day "))
    minute = int(result.split()[1])
    assert 0 <= minute <= 59


@given(st.none())
def test_schedule_slot_rejects_none(value):
    with pytest.raises(TypeError):
        schedule_slot(value)


@given(st.floats(min_value=-100, max_value=500,
                 allow_nan=False, allow_infinity=False))
def test_celsius_round_trip(value):
    assert parse_setpoint(f"{value}C") == round(value, 1)


@given(st.lists(st.floats(min_value=-100, max_value=500,
                          allow_nan=False, allow_infinity=False),
                min_size=1, max_size=30))
def test_average_matches_python_mean(values):
    csv = ",".join(str(value) for value in values)
    assert average_temperature(csv) == pytest.approx(sum(values) / len(values))


@given(st.integers(min_value=0, max_value=23),
       st.integers(min_value=0, max_value=59))
def test_schedule_valid_time(hour, minute):
    result = schedule_slot(f"{hour:02d}:{minute:02d}")
    expected = "night" if hour < 6 else "day"
    assert result == f"{expected} {minute}"


@pytest.mark.parametrize("value", ["", "21", "21K", "abcC", "21Cjunk"])
def test_invalid_setpoints(value):
    with pytest.raises(ValueError):
        parse_setpoint(value)


@pytest.mark.parametrize("value", ["", "1,,2", "a,2", ",", "1,"])
def test_invalid_readings(value):
    with pytest.raises(ValueError):
        average_temperature(value)


@pytest.mark.parametrize("value", ["", "7:3", "24:00", "12:60",
                                   "1:02", "ab:cd", "12-30"])
def test_invalid_times(value):
    with pytest.raises(ValueError):
        schedule_slot(value)


def test_fahrenheit_conversion():
    assert parse_setpoint("70F") == 21.1


def test_schedule_night_boundary():
    assert schedule_slot("05:59") == "night 59"


def test_schedule_day_boundary():
    assert schedule_slot("06:00") == "day 0"
