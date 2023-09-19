people = int(input())
days = int(input())
cards_number = int(input())
tickets = int(input())

days_price = days * 20
cards_price = cards_number * 1.6
price_tickets = tickets * 6
total_price = people * (days_price + cards_price + price_tickets) * 1.25

print(f'{total_price:.2f}')