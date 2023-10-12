def even_numbers():
    input_string = [i for i, x in enumerate(input().split(', ')) if int(x) % 2 == 0]
    return input_string


print(even_numbers())
