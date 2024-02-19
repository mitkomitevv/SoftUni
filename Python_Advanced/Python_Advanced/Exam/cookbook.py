def cookbook(*recipies):
    recipies_dict = {}

    for recipie, cuisine, ingredients in recipies:
        if cuisine not in recipies_dict:
            recipies_dict[cuisine] = {}
        recipies_dict[cuisine].update({recipie: ingredients})

    sorted_recipies = dict(sorted(recipies_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in sorted_recipies.items():
        sorted_recipies[k] = sorted(v.items(), key=lambda x: x[0])

    result = ""
    for key, values in sorted_recipies.items():
        result += f"{key} cuisine contains {len(values)} recipes:\n"
        for rec, products in values:
            result += f"  * {rec} -> Ingredients: {', '.join(products)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
