import random

def generate_telemetry(last_name, seed_num, favorite_artist, count=10):
    # Create a unique seed using student information
    unique_seed = seed_num + sum(ord(c) for c in last_name) + sum(ord(c) for c in favorite_artist)
    random.seed(unique_seed)

    for i in range(count):
        # Occasionally generate an invalid value
        if i == 7:
            yield None
        else:
            yield round(random.uniform(40, 100), 2)