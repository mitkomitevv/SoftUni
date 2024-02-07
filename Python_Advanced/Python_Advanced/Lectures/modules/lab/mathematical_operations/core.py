def add(n1, n2):
    print(f"{n1 + n2:.2f}")

def subtract(n1, n2):
    print(f"{n1 - n2:.2f}")

def multiply(n1, n2):
    print(f"{n1 * n2:.2f}")

def divide(n1, n2):
    try:
        print(f"{n1 / n2:.2f}")
    except ZeroDivisionError:
        print("You Can't divide with zero")

def power(n1, n2):
    print(f"{n1 ** n2:.2f}")
