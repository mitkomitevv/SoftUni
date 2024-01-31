def accommodate_new_pets(capacity, max_weight, *pets):
    cap = capacity
    accommodated = {}
    result = []

    for pet, weight in pets:
        if cap <= 0:
            result.append("You did not manage to accommodate all pets!\nAccommodated pets:")
            break
        if weight > max_weight:
            continue
        if pet not in accommodated:
            accommodated[pet] = 0
        accommodated[pet] += 1
        cap -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {cap}.\nAccommodated pets:")

    sorted_pets = dict(sorted(accommodated.items()))

    return '\n'.join(result + [f"{pet}: {count}" for pet, count in sorted_pets.items()])


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
