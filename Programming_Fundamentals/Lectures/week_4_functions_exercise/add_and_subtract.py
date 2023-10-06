"""Adding an subtracting."""


def sum_numbers(first, second: int) -> int:
    return first + second


def subtract(result, third: int) -> int:
    return result - third


def add_and_subtract(first, second, third: int) -> int:
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))
