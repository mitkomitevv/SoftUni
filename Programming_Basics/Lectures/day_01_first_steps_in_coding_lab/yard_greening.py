number_of_square_meters = float(input())
price_for_square_meter = 7.61

done_yard = number_of_square_meters * price_for_square_meter
discount = done_yard * 0.18
final_price = done_yard - discount

print(done_yard)
print(final_price)
print(discount)
