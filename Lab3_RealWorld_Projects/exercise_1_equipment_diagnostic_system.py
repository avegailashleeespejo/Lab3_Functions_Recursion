# EQUIPMENT DIAGNOSTIC SYSTEM

LAST_NAME = "Espejo"
SEED_NUM = 9
FAVORITE_ARTIST = "Cup of Joe"

import random
from functools import wraps

# --------------------------------
# DECORATOR: Records diagnostic process
# --------------------------------
def diagnostic_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed: {func.__name__}")
        return result
    return wrapper


# --------------------------------
# GENERATE EQUIPMENT READINGS
# --------------------------------
def generate_readings():
    # Create a unique seed from the required student information
    unique_seed = SEED_NUM + len(LAST_NAME) + len(FAVORITE_ARTIST)
    random.seed(unique_seed)

    readings = {
        "Temperature": random.uniform(40, 100),
        "Pressure": random.uniform(20, 80),
        "Voltage": random.uniform(180, 250),
        "Vibration": random.uniform(0, 10)
    }

    return readings


# --------------------------------
# VALIDATION FUNCTION
# --------------------------------
@diagnostic_log
def validate_reading(name, value):
    try:
        if not isinstance(value, (int, float)):
            raise ValueError("Reading is not a number.")

        if value < 0:
            raise ValueError("Reading cannot be negative.")

        return True

    except ValueError as error:
        print(f"[INVALID] {name}: {error}")
        return False


# --------------------------------
# CALCULATION FUNCTION
# --------------------------------
@diagnostic_log
def calculate_average(readings):
    if not readings:
        return 0

    return sum(readings.values()) / len(readings)


# --------------------------------
# CLASSIFICATION FUNCTION
# --------------------------------
@diagnostic_log
def classify_equipment(readings):
    # Check each equipment reading against its safe range
    if readings["Temperature"] > 90:
        return "WARNING"

    if readings["Pressure"] > 70:
        return "WARNING"

    if readings["Voltage"] > 240:
        return "WARNING"

    if readings["Vibration"] > 8:
        return "WARNING"

    return "NORMAL"


# --------------------------------
# MAIN PROGRAM
# --------------------------------
def main():
    print("=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generate data
    generated_data = generate_readings()

    print("\n--- Generated Equipment Data ---")
    for name, value in generated_data.items():
        print(f"{name}: {value:.2f}")

    # Validate data
    valid_data = {}

    print("\n--- Validation Results ---")
    for name, value in generated_data.items():
        if validate_reading(name, value):
            valid_data[name] = value
            print(f"{name}: VALID")
        else:
            print(f"{name}: INVALID")

    # Process valid data
    print("\n--- Diagnostic Results ---")

    if valid_data:
        average = calculate_average(valid_data)
        condition = classify_equipment(valid_data)

        print(f"Average Reading: {average:.2f}")
        print(f"Equipment Condition: {condition}")
    else:
        print("No valid readings available.")

    # Final summary
    print("\n--- Final Output ---")
    print(f"Total Readings: {len(generated_data)}")
    print(f"Valid Readings: {len(valid_data)}")
    print(f"Invalid Readings: {len(generated_data) - len(valid_data)}")

    if valid_data:
        print(f"Final Diagnosis: {condition}")
    else:
        print("Final Diagnosis: Unable to determine")


# Run program
if __name__ == "__main__":
    main()