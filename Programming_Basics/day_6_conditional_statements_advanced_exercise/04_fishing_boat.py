budget = int(input())
season = input()
number_fisherman = int(input())
rent_ship = 0

if season == 'Spring':
    rent_ship = 3000
    if number_fisherman <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < number_fisherman <= 11:
        rent_ship = rent_ship * 0.85
    elif number_fisherman > 11:
        rent_ship = rent_ship * 0.75

if season == 'Summer' or season == 'Autumn':
    rent_ship = 4200
    if number_fisherman <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < number_fisherman <= 11:
        rent_ship = rent_ship * 0.85
    elif number_fisherman > 11:
        rent_ship = rent_ship * 0.75

if season == 'Winter':
    rent_ship = 2600
    if number_fisherman <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < number_fisherman <= 11:
        rent_ship = rent_ship * 0.85
    elif number_fisherman > 11:
        rent_ship = rent_ship * 0.75

if season != "Autumn" and number_fisherman % 2 == 0:
    rent_ship = rent_ship * 0.95

diff = abs(budget - rent_ship)

if budget >= rent_ship:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
