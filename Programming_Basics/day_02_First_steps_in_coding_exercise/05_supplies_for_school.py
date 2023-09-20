pen_number = int(input())
marker_number = int(input())
detur_lt = int(input())
discount = int(input())

pen_price = pen_number * 5.80
marker_price = marker_number *7.20
detur_price = detur_lt *1.2

total_price = pen_price + marker_price + detur_price
total_discount = discount / 100

price_with_discount = total_price - (total_price * total_discount)

print(price_with_discount)
