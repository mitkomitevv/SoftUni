def perfect_number(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += i
    if num == counter:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
perfect_or_not = perfect_number(number)
print(perfect_or_not)
