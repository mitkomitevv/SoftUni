dog_food_packages = int(input())
cat_food_packages = int(input())

dog_food = 2.50
cat_food = 4

price_for_dogs = dog_food_packages * dog_food
price_for_cats = cat_food_packages * cat_food

total_price = price_for_dogs + price_for_cats

print(f'{total_price} lv.')