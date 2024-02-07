from Python_Advanced.Python_Advanced.Lectures.modules.lab.mathematical_operations.core import *

num1, sign, num2 = input().split()
num1, num2 = float(num1), int(num2)

if sign == '+':
    add(num1, num2)
elif sign == '-':
    subtract(num1, num2)
elif sign == '*':
    multiply(num1, num2)
elif sign == '/':
    divide(num1, num2)
elif sign == '^':
    power(num1, num2)
