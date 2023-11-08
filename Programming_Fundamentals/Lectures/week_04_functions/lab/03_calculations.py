operator = input()
num_1 = int(input())
num_2 = int(input())


def result():
    if operator == 'add':
        return num_1 + num_2
    elif operator == 'subtract':
        return num_1 - num_2
    elif operator == 'multiply':
        return num_1 * num_2
    elif operator == 'divide':
        return num_1 / num_2


print(int(result()))
