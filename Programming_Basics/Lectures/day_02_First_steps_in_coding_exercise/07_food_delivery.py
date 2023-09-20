chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
veg_price = veg_menu * 8.15

total_for_menu = chicken_price + fish_price + veg_price
desert = total_for_menu * 0.2

final_price = total_for_menu + desert +2.50

print(final_price)