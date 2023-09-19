n_1 = int(input())
n_2 = int(input())
operator = input()

result = 0
flag = False

if operator == "+":
    result = n_1 + n_2
elif operator == "-":
    result = n_1 - n_2
elif operator == "*":
    result = n_1 * n_2
elif operator == "/":
    if n_2 == 0:
        flag = True
    else:
        result = n_1 / n_2
elif operator == "%":
    if n_2 == 0:
        flag = True
    else:
        result = n_1 % n_2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        print(f"{n_1} {operator} {n_2} = {result} - even")
    else:
        print(f"{n_1} {operator} {n_2} = {result} - odd")
elif operator == "/":
    if flag:
        print(f"Cannot divide {n_1} by zero")
    else:
        print(f"{n_1} {operator} {n_2} = {result:.2f}")
elif operator == "%":
    if flag:
        print(f"Cannot divide {n_1} by zero")
    else:
        print(f"{n_1} {operator} {n_2} = {result}")

