from math import log

first = int(input())

try:
    second = int(input())
    print(f"{log(first, second):.2f}")
except ValueError:
    print(f"{log(first):.2f}")
