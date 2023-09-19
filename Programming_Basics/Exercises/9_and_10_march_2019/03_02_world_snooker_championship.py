stage = input()
ticket = input()
count_ticket = int(input())
picture = input()

ticket_price = 0

if stage == 'Quarter final':
    if ticket == 'Standard':
        ticket_price = 55.50
    elif ticket == 'Premium':
        ticket_price = 105.20
    elif ticket == 'VIP':
        ticket_price = 118.90

if stage == 'Semi final':
    if ticket == 'Standard':
        ticket_price = 75.88
    elif ticket == 'Premium':
        ticket_price = 125.22
    elif ticket == 'VIP':
        ticket_price = 300.40

if stage == 'Final':
    if ticket == 'Standard':
        ticket_price = 110.10
    elif ticket == 'Premium':
        ticket_price = 160.66
    elif ticket == 'VIP':
        ticket_price = 400

total_price = count_ticket * ticket_price

if total_price > 4000:
    total_price = total_price * 0.75
    picture = 'N'
elif total_price > 2500:
    total_price = total_price * 0.90

if picture == 'Y':
    total_price = total_price + (count_ticket * 40)

print(f'{total_price:.2f}')