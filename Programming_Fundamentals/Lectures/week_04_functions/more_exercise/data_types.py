def operation(int_real_str, num_float_str):
    if int_real_str == 'int':
        result = int(num_float_str) * 2
    elif int_real_str == 'real':
        result = f'{float(num_float_str) * 1.5:.2f}'
    else:
        result = f'${num_float_str}$'
    return result


input1 = input()
input2 = input()
print(operation(input1, input2))
