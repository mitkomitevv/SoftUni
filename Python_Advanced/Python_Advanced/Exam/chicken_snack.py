from collections import deque

amount_money = deque(int(x) for x in input().split())
prices = deque(int(x) for x in input().split())
food = 0

while amount_money and prices:
    money, price = amount_money.pop(), prices.popleft()

    if money == price:
        food += 1
    elif money > price:
        food += 1
        if amount_money:
            change = money - price
            amount_money[-1] += change

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
elif 0 < food < 4:
    print(f"Henry ate: {food} food." if food == 1 else f"Henry ate: {food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
