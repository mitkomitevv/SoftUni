input_line = input()
my_dict = {}
while input_line != 'statistics':
    product, quantity = input_line.split(': ')
    quantity = int(quantity)
    if product in my_dict:
        my_dict[product] += quantity
    else:
        my_dict[product] = quantity

    input_line = input()

print('Products in stock:')
for key, value in my_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")