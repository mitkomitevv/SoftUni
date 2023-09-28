lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broken = 0
for current_fight in range(1, lost_fights + 1):
    if current_fight % 2 == 0:
        expenses += helmet_price
    if current_fight % 3 == 0:
        expenses += sword_price
        if current_fight % 2 == 0:
            expenses += shield_price
            shield_broken += 1
    if shield_broken == 2:
        expenses += armor_price
    if shield_broken == 2:
        shield_broken = 0
print(f'Gladiator expenses: {expenses:.2f} aureus')
