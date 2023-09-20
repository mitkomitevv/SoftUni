flower_type = input()
flower_count = int(input())
budget = int(input())

price_flower = 0

if flower_type == "Roses":
    price_flower = 5
    if flower_count > 80:
        price_flower = price_flower * 0.9
elif flower_type == "Dahlias":
    price_flower = 3.80
    if flower_count > 90:
        price_flower = price_flower * 0.85
elif flower_type == "Tulips":
    price_flower = 2.80
    if flower_count > 80:
        price_flower = price_flower * 0.85
elif flower_type == "Narcissus":
    price_flower = 3
    if flower_count < 120:
        price_flower = price_flower * 1.15
elif flower_type == "Gladiolus":
    price_flower = 2.50
    if flower_count < 80:
        price_flower = price_flower * 1.20

total = flower_count * price_flower
diff = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")