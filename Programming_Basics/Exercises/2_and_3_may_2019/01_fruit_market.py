straw_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
straw_kg = float(input())

straw_total = straw_kg * straw_price
rasp_total = straw_price / 2
orange_total = rasp_total - (rasp_total * 0.4)
bananas_total = rasp_total - (rasp_total * 0.8)

total = straw_total + (rasp_total * raspberry_kg) + (orange_total * orange_kg) + (bananas_total * bananas_kg)

print(f"{total:.2f}")