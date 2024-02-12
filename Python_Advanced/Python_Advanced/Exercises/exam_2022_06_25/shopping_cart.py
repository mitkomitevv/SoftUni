def shopping_cart(*products_info):
    products = {
        "Soup": [3],
        "Pizza": [4],
        "Dessert": [2]
    }

    for line in products_info:
        if line == 'Stop':
            break
        meal, product = line
        if product not in products[meal] and products[meal][0] > 0:
            products[meal].append(product)
            products[meal][0] -= 1

    products = {key: value[1:] for key, value in products.items()}

    if all(not value for value in products.values()):
        return "No products in the cart!"

    products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for meal, ingredients in products:
        ingredients.sort()
        # noinspection PyTypeChecker
        products_part = "\n - ".join(ingredients)
        result += f"{meal}:\n - {products_part}\n" if ingredients else f"{meal}:\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
