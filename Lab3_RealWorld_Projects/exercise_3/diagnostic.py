from functools import wraps

# Decorator for monitoring the processing function
def monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}")
        return result

    return wrapper


# Validate telemetry data
def validate(value):
    try:
        if value is None:
            raise ValueError("Invalid telemetry value.")

        if not isinstance(value, (int, float)):
            raise ValueError("Telemetry must be numeric.")

        if value < 0:
            raise ValueError("Telemetry cannot be negative.")

        return True

    except ValueError as error:
        print(f"[INVALID] {error}")
        return False


# Recursively analyze an abnormal reading
def recursive_analysis(value, level=1):
    print(f"[LOG] Recursive analysis level {level}: {value}")

    # Base condition
    if value <= 50 or level >= 3:
        return f"Analysis stopped at level {level}"

    return recursive_analysis(value - 10, level + 1)


# Process telemetry using a lambda function
@monitor
def process_data(readings):
    # Lambda transforms the readings
    transform = lambda x: round(x * 1.05, 2)

    processed = []
    abnormal = []

    for value in readings:
        if validate(value):
            new_value = transform(value)
            processed.append(new_value)

            if new_value > 90:
                abnormal.append(new_value)
                recursive_analysis(new_value)

    return processed, abnormal