budget = float(input())
season = input()

spent = 0
sleeping = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == 'summer':
        spent = budget * 0.3
        sleeping = "Camp"
    elif season == 'winter':
        spent = budget * 0.7
        sleeping = "Hotel"

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == 'summer':
        spent = budget * 0.4
        sleeping = "Camp"
    elif season == 'winter':
        spent = budget * 0.8
        sleeping = "Hotel"

elif budget > 1000:
    destination = "Europe"
    spent = budget * 0.9
    sleeping = "Hotel"

print(f"Somewhere in {destination}")
print(f"{sleeping} - {spent:.2f}")