numbers = [int(x) for x in input().split()]
set_one = set()
set_two = set()

for _ in range(numbers[0]):
    num = int(input())
    set_one.add(num)

for _ in range(numbers[1]):
    num = int(input())
    set_two.add(num)

for num in set_one.intersection(set_two):
    print(num)
