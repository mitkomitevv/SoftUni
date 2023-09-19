name_of_film = input()
days_number = int(input())
tickets_number = int(input())
price_ticket = float(input())
cinema_percent = int(input())

tickets_for_day = tickets_number * price_ticket
total_money = days_number * tickets_for_day
money_for_cinema = total_money * cinema_percent / 100

total_studio = total_money - money_for_cinema

print(f"The profit from the movie {name_of_film} is {total_studio:.2f} lv.")
