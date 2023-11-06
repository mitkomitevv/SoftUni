products = input()
my_dict = {}
while products != 'buy':
    name, price, quantity = products.split()
    price, quantity = float(price), int(quantity)
    if name not in my_dict:
        my_dict[name] = [price, quantity]
    else:
        my_dict[name][0] = price
        my_dict[name][1] += quantity

    products = input()

for product in my_dict.keys():
    my_dict[product] = my_dict[product][0] * my_dict[product][1]
    print(f"{product} -> {my_dict[product]:.2f}")