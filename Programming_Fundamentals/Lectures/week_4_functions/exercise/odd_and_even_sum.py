def result(num_as_string: str):
    even_sum = 0
    odd_sum = 0
    for num in num_as_string:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    return odd_sum, even_sum


number = input()
odd_final_sum, even_final_sum = result(number)
print(f'Odd sum = {odd_final_sum}, Even sum = {even_final_sum}')
