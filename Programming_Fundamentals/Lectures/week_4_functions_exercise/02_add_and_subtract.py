num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def add_and_subtract():
    def sum_numbers():
        return num_1 + num_2

    def subtract():
        return sum_numbers() - num_3

    return subtract()


print(add_and_subtract())

# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# sum_elements = num_1 + num_2 - num_3
# print(sum_elements)
