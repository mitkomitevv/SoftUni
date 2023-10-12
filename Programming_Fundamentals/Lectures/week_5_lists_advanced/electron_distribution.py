def electron_distribution(num):
    shells = []
    remaining_electrons = num
    n = 1
    while remaining_electrons > 0:
        max_electrons = 2 * n ** 2
        if remaining_electrons >= max_electrons:
            shells.append(max_electrons)
            remaining_electrons -= max_electrons
        else:
            shells.append(remaining_electrons)
            break
        n += 1
    return shells


number = int(input())
print(electron_distribution(number))
