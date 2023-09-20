needed_money = float(input())
available_sum = float(input())
spend_days = 0
all_days = 0
while True:
    action = input()
    current_sum = float(input())
    all_days += 1
    if action == "spend":
        spend_days += 1
        available_sum -= current_sum
        if available_sum < 0:
            available_sum = 0

    if spend_days == 5:
        print(f"You can't save the money.")
        print(all_days)
        break

    if action == 'save':
        available_sum += current_sum
        spend_days = 0

    if available_sum >= needed_money:
        print(f'You saved the money for {all_days} days.')
        break
