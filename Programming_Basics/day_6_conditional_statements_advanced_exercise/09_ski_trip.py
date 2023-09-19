stay_days = int(input())
place = input()
grade = input()
price = 0
sleep = stay_days - 1

if place == "room for one person":
    price = sleep * 18

elif place == "apartment":
    if sleep < 10:
        price = (sleep * 25) * 0.7
    elif 10 <= sleep <= 15:
        price = (sleep * 25) * 0.65
    else:
        price = (sleep * 25) * 0.5

elif place == "president apartment":
    if sleep < 10:
        price = (sleep * 35) * 0.9
    elif 10 >= sleep >= 15:
        price = (sleep * 35) * 0.85
    else:
        price = (sleep * 35) * 0.8

if grade == "positive":
    price = price * 1.25
elif grade == "negative":
    price = price * 0.90

print(f"{price:.2f}")