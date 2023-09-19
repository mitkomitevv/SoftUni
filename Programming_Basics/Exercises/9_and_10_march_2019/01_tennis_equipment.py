import math

racket_price = float(input())
count_racket = int(input())
count_shoes = int(input())

racket_total = racket_price * count_racket
shoes_price = racket_price / 6
shoes_total = shoes_price * count_shoes
rackets_plus_shoes = racket_total + shoes_total

other_expenses = rackets_plus_shoes * 0.2

total_expenses = rackets_plus_shoes + other_expenses

djoko_price = math.floor(total_expenses / 8)
sponsor_price = math.ceil(total_expenses * 0.875)

print(f"Price to be paid by Djokovic {djoko_price}")
print(f"Price to be paid by sponsors {sponsor_price}")