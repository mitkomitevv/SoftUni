products = input().split()

my_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    quantity = int(products[i + 1])
    my_dict[key] = quantity

print(my_dict)