input_line = input()

prime_sum = 0
non_prime_sum = 0
while input_line != 'stop':
    number = int(input_line)

    if number < 0:
        print('Number is negative.')
        input_line = input()
        continue

    for i in range(2, number):
        if number % i == 0:
            non_prime_sum += number
            break
    else:
        prime_sum += number
    input_line = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
