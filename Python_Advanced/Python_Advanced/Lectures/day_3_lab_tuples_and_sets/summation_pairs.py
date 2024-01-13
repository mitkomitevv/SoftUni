numbers = [int(x) for x in input().split()]
target = int(input())

targets = set()
values = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values[value]
        del values[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values[resulting_number] = value


# for i in range(len(numbers)):
#     if numbers[i] == '':
#         continue
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] == '':
#             continue
#         if numbers[i] + numbers[j] == target:
#             print(f"{numbers[i]} + {numbers[j]} = {target}")
#             numbers[i] = ''
#             numbers[j] = ''
#             break
