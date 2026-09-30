from telemetry_generator import generate_telemetry
from diagnostic import process_data


# Student-specific information
LAST_NAME = "Espejo"
SEED_NUM = 9
FAVORITE_ARTIST = "Cup of Joe"


def main():

    print("======================================")
    print(" INTELLIGENT EQUIPMENT MONITORING")
    print("======================================")

    print("\n--- Student-Specific Inputs ---")
    print(f"Last Name: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generate telemetry using a generator
    telemetry = generate_telemetry(
        LAST_NAME,
        SEED_NUM,
        FAVORITE_ARTIST,
        10
    )

    print("\n--- Generated Telemetry Data ---")

    # Convert only the generated values needed for processing
    readings = []

    for value in telemetry:
        print(value)
        readings.append(value)

    # Process telemetry
    print("\n--- Processing Results ---")

    processed, abnormal = process_data(readings)

    # Count valid and invalid readings
    valid_count = len(processed)
    total_count = len(readings)
    invalid_count = total_count - valid_count
    abnormal_count = len(abnormal)

    # Determine equipment status
    if abnormal_count > 0:
        status = "WARNING - ABNORMAL CONDITION DETECTED"
    else:
        status = "NORMAL"

    # Final diagnostic report
    print("\n--- Final Diagnostic Summary ---")
    print(f"Processed Readings: {total_count}")
    print(f"Valid Readings: {valid_count}")
    print(f"Invalid Readings: {invalid_count}")
    print(f"Abnormal Conditions: {abnormal_count}")
    print(f"Overall Equipment Status: {status}")

    print("\n--- Processed Results ---")
    print(processed)

    print("\n--- Final Output ---")
    print("Diagnostic report generated successfully.")


if __name__ == "__main__":
    main()