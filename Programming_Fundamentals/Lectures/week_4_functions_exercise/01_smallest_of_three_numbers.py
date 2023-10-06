def smallest(n1, n2, n3):
    smallest_number = min(n1, n2, n3)
    return smallest_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest(first_number, second_number, third_number))
