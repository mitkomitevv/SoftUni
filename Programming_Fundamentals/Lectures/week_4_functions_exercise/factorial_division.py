def factorial(num):
    for i in range(1, num):
        num *= i
    return num


first_number = int(input())
second_number = int(input())
num1_result = factorial(first_number)
num2_result = factorial(second_number)
divided = num1_result / num2_result
print(f'{divided:.2f}')
