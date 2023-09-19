from math import ceil

bread_number = int(input())

sugar = 0
flour = 0
max_sugar = 0
max_flour = 0

for _ in range(bread_number):
    sugar_needed = int(input())
    flour_needed = int(input())

    if sugar_needed > max_sugar:
        max_sugar = sugar_needed
    if flour_needed > max_flour:
        max_flour = flour_needed

    sugar += sugar_needed
    flour += flour_needed

sugar_packets = ceil(sugar / 950)
flour_packets = ceil(flour / 750)

print(f'Sugar: {sugar_packets}')
print(f'Flour: {flour_packets}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
