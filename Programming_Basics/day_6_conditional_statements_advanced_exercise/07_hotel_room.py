month = input()
overnight_stay = int(input())

price = 0

if month == "May" or month == "October":
    app_price = 65
    studio_price = 50
    if 7 < overnight_stay <= 14:
        studio_price = 50 * 0.95
    elif overnight_stay > 14:
        studio_price = 50 * 0.70
        app_price = 65 * 0.90

if month == "June" or month == "September":
    app_price = 68.70
    studio_price = 75.2
    if overnight_stay > 14:
        studio_price = 75.2 * 0.80
        app_price = 68.70 * 0.90

if month == "July" or month == "August":
    studio_price = 76
    app_price = 77
    if overnight_stay > 14:
        app_price = 77 * 0.90

total_studio = overnight_stay * studio_price
total_app = overnight_stay * app_price

print(f"Apartment: {total_app:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
