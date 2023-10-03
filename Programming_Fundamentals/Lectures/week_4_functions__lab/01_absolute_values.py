def formatted():
    sequence = input().split(' ')
    numbers = [float(x) for x in sequence]
    formatted_numbers = [abs(y) for y in numbers]
    return formatted_numbers


print(formatted())
