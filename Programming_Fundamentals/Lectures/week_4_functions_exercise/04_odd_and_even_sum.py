number = input()


def result():
    # even_sum = [x for x in range(number) if x % 2 == 0]
    # odd_sum = [x for x in range(number) if x % 2 != 0]
    even_sum = 0
    odd_sum = 0
    for i in range(len(number)):
        if int(number[i]) % 2 == 0:
            even_sum += int(number[i])
        elif int(number[i]) % 2 == 1:
            odd_sum += int(number[i])

    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


result()
