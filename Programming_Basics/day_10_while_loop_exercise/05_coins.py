change = float(input())
coins_counter = 0
change_coins = int(change * 100)
while change_coins != 0:
    if change_coins >= 200:
        change_coins -= 200
    elif change_coins >= 100:
        change_coins -= 100
    elif change_coins >= 50:
        change_coins -= 50
    elif change_coins >= 20:
        change_coins -= 20
    elif change_coins >= 10:
        change_coins -= 10
    elif change_coins >= 5:
        change_coins -= 5
    elif change_coins >= 2:
        change_coins -= 2
    elif change_coins >= 1:
        change_coins -= 1

    coins_counter += 1

print(coins_counter)
