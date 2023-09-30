list_numbers = list(map(int, input().split()))
n = int(input())
for i in range(n):
    largest_number = max(list_numbers)
    smallest_number = min(list_numbers)
    list_numbers.remove(smallest_number)
result = ', '.join(map(str, list_numbers))
print(result)
