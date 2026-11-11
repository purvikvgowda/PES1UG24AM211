"""Validated smart thermostat input-processing functions."""


def _require_text(value, field):
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string")
    if not value.strip():
        raise ValueError(f"{field} cannot be empty")


def parse_setpoint(text):
    """Parse a Celsius or Fahrenheit setpoint, returning Celsius to 1 d.p."""
    _require_text(text, "setpoint")
    text = text.strip()
    if len(text) < 2:
        raise ValueError("setpoint must include a number and C or F unit")

    unit = text[-1].upper()
    if unit not in {"C", "F"}:
        raise ValueError("temperature unit must be C or F")
    number = text[:-1].strip()
    try:
        value = float(number)
    except ValueError as exc:
        raise ValueError("temperature value must be numeric") from exc
    if not (-273.15 <= value <= 1000):
        raise ValueError("temperature is outside the supported range")
    if unit == "F":
        value = (value - 32) * 5 / 9
    return round(value, 1)


def average_temperature(readings_csv):
    """Return the mean of a non-empty comma-separated list of temperatures."""
    _require_text(readings_csv, "readings")
    parts = readings_csv.split(",")
    if any(not part.strip() for part in parts):
        raise ValueError("readings must not contain empty values")
    try:
        values = [float(part.strip()) for part in parts]
    except ValueError as exc:
        raise ValueError("all readings must be numeric") from exc
    if any(not (-273.15 <= value <= 1000) for value in values):
        raise ValueError("a reading is outside the supported range")
    return sum(values) / len(values)


def schedule_slot(time_text):
    """Classify a strict 24-hour HH:MM time as night or day."""
    _require_text(time_text, "time")
    time_text = time_text.strip()
    parts = time_text.split(":")
    if len(parts) != 2 or any(len(part) != 2 or not part.isdigit()
                              for part in parts):
        raise ValueError("time must use HH:MM format")
    hour, minute = (int(part) for part in parts)
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError("time is outside the 24-hour clock")
    if hour < 6:
        return f"night {minute}"
    return f"day {minute}"


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    try:
        print("Setpoint in Celsius:", parse_setpoint(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid setpoint:", exc)
        return

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    try:
        print("Average Temperature:", average_temperature(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid readings:", exc)
        return

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    try:
        print("Schedule Slot:", schedule_slot(user_input))
    except (TypeError, ValueError) as exc:
        print("Invalid time:", exc)


if __name__ == "__main__":
    main()
