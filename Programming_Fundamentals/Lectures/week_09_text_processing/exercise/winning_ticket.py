tickets = input().split(', ')
winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_part, right_part = ticket[:10], ticket[10:]

    match = False
    for symbol in winning_symbols:
        for match_length in range(10, 5, -1):
            repetition = symbol * match_length
            if repetition in left_part and repetition in right_part:
                if match_length == 10:
                    print(f'ticket "{ticket}" - {match_length}{symbol} Jackpot!')
                elif 6 <= match_length <= 9:
                    print(f'ticket "{ticket}" - {match_length}{symbol}')
                match = True
                break
    if not match:
        print(f'ticket "{ticket}" - no match')
