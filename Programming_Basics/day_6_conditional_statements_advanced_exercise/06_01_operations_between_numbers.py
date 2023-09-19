import sys

n_1 = int(input())
n_2 = int(input())
operator = input()

result = 0
even_or_odd = ""
wrong = False

if operator == "+":
    result = n_1 + n_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = "odd"
    print(f"{n_1} + {n_2} = {result} - {even_or_odd}")

elif operator == "-":
    result = n_1 - n_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = "odd"
    print(f"{n_1} - {n_2} = {result} - {even_or_odd}")

elif operator == "*":
    result = n_1 * n_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = "odd"
    print(f"{n_1} * {n_2} = {result} - {even_or_odd}")


if operator == "/":
    if n_2 == 0:
        wrong = True
        print(f"Cannot divide {n_1} by zero")
    else:
        result = n_1 / n_2
        print(f"{n_1} / {n_2} = {result:.2f}")

if operator == "%":
    if n_2 == 0:
        wrong = True
        print(f"Cannot divide {n_1} by zero")
    else:
        result = n_1 % n_2
        print(f"{n_1} % {n_2} = {result}")


