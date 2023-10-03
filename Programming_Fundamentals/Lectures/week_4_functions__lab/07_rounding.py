input_line = input().split()
my_list = []


def rounded():
    for n in input_line:
        num = round(float(n))
        my_list.append(num)
    return my_list


print(rounded())
