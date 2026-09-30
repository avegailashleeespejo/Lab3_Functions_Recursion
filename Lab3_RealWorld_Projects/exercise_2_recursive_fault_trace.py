# RECURSIVE FAULT TRACE

LAST_NAME = "Espejo"
SEED_NUM = 9
FAVORITE_ARTIST = "Cup of Joe"

# --------------------------------
# GENERATE STUDENT-SPECIFIC FAULT CODE
# --------------------------------
def generate_fault_code():
    name_value = sum(ord(char) for char in LAST_NAME)
    artist_value = sum(ord(char) for char in FAVORITE_ARTIST)

    fault_code = (name_value + artist_value + SEED_NUM) % 100
    return fault_code


# --------------------------------
# RECURSIVE FAULT TRACE
# --------------------------------
def fault_trace(code, trace=None, calls=0):
    if trace is None:
        trace = []

    calls += 1
    trace.append(code)

    print(f"[LOG] Recursive call {calls}: Fault code = {code}")

    # Base condition
    if code <= 1:
        return trace, calls

    # Reduce the fault code for the next recursive call
    next_code = code // 2

    return fault_trace(next_code, trace, calls)


# --------------------------------
# MAIN PROGRAM
# --------------------------------
def main():
    print("=== RECURSIVE FAULT TRACE ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generate fault code
    fault_code = generate_fault_code()

    print("\n--- Generated Fault Data ---")
    print(f"Generated Fault Code: {fault_code}")

    # Perform recursive trace
    print("\n--- Recursive Trace ---")
    trace, calls = fault_trace(fault_code)

    # Display results
    print("\n--- Number of Recursive Calls ---")
    print(f"Total Calls: {calls}")

    print("\n--- Final Output ---")
    print("Complete Fault Trace:", " -> ".join(map(str, trace)))
    print(f"Final Result: Fault code reached termination condition ({trace[-1]}).")


# Run the program
if __name__ == "__main__":
    main()