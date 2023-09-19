nylon_amount = int(input())
paint_lt = int(input())
razr_lt = int(input())
hours_workers = int(input())

nylon_price = (nylon_amount + 2) * 1.5
paint_price = (paint_lt * 1.1) * 14.50
razr_price = razr_lt * 5

materials_sum = nylon_price + paint_price + razr_price + 0.40
money_for_workers = (materials_sum * 0.3) * hours_workers

final_price = materials_sum + money_for_workers

print(final_price)

