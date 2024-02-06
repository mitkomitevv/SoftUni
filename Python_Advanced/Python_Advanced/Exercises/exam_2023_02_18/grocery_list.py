def shop_from_grocery_list(budget, grocery_list, *args):
    bought_products = []
    remaining_budget = budget

    for product, price in args:
        if product not in bought_products and product in grocery_list:
            if remaining_budget >= price:
                bought_products.append(product)
                grocery_list.remove(product)
                remaining_budget -= price
            else:
                break
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {remaining_budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
