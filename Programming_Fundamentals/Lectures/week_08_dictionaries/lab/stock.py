input_line = input().split()

my_dict = {}

for i in range(0,len(input_line), 2):
    key = input_line[i]
    quantity = input_line[i + 1]
    my_dict[key] = quantity

products_to_search = input().split()

for product in products_to_search:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")