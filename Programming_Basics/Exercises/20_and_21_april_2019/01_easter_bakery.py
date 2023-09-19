flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_count = int(input())
yeast_packet = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2

flour = flour_price * flour_kg
sugar = sugar_price * sugar_kg
eggs = eggs_count * eggs_price
yeast = yeast_packet * yeast_price

total = flour + sugar + eggs + yeast

print(f"{total:.2f}")