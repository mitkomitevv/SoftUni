days = int(input())
number_players = int(input())
energy = float(input())
water_for_one = float(input())
food_for_one = float(input())
total_water = days * number_players * water_for_one
total_food = days * number_players * food_for_one
flag = False
for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        flag = True
        break
    if day % 2 == 0:
        energy = energy * 1.05
        total_water *= 0.70
    if day % 3 == 0:
        total_food -= total_food / number_players
        energy = energy * 1.1

if flag:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
