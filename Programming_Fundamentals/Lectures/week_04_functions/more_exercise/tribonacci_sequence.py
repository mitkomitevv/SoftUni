def tribonacci(number):
    if number == 0:
        return []
    elif number == 1:
        return [1]
    elif number == 2:
        return [1, 1]
    elif number == 3:
        return [1, 1, 2]

    sequence = [1, 1, 2]
    while len(sequence) < number:
        final = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(final)
    return sequence


num = int(input())
result = tribonacci(num)
print(*result)
