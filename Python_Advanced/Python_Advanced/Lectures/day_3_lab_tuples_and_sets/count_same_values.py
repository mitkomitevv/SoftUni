numbers = tuple(float(x) for x in input().split())
my_dict = {}

for num in numbers:
    if num not in my_dict:
        my_dict[num] = numbers.count(num)

for number, count in my_dict.items():
    print(f"{number} - {count} times")
