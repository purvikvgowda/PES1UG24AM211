
from thermostat_control import (
    target_temperature,
    hvac_action,
    energy_alert,
)


# Target temperature tests
def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_night():
    assert target_temperature("sleep", True, 2) == 18


def test_sleep_mode_day():
    assert target_temperature("sleep", True, 12) == 20


def test_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_morning_temperature():
    assert target_temperature("home", True, 7) == 22


def test_evening_temperature():
    assert target_temperature("home", True, 19) == 21


def test_default_temperature():
    assert target_temperature("home", True, 12) == 20


def test_morning_boundary():
    assert target_temperature("home", True, 9) == 20


def test_evening_boundary():
    assert target_temperature("home", True, 22) == 20


# HVAC action tests
def test_hvac_idle():
    assert hvac_action(20, 20.5, 10) == "idle"


def test_hvac_heat_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool():
    assert hvac_action(25, 20, 25) == "cool"


def test_hvac_idle_negative_difference():
    assert hvac_action(20.5, 20, 10) == "idle"


def test_hvac_outside_boundary():
    assert hvac_action(25, 20, 30) == "cool"


# Energy alert tests
def test_energy_no_readings():
    assert energy_alert([], 10) == "ok"


def test_energy_all_below_limit():
    assert energy_alert([2, 5, 8], 10) == "ok"


def test_energy_critical():
    assert energy_alert([11, 12, 3], 10) == "critical"


def test_energy_warning():
    assert energy_alert([11, 3], 10) == "warning"


def test_energy_exact_limit():
    assert energy_alert([10, 5], 10) == "ok"
