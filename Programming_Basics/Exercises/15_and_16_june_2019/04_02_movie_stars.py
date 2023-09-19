budget = float(input())
money_needed = budget
salary = 0

input_line = input()
while input_line != 'ACTION':
    actor = input_line

    if len(actor) <= 15:
        salary = float(input())

    if len(actor) > 15:
        salary = money_needed * 0.2

    money_needed -= salary

    if money_needed < 0:
        break

    input_line = input()

diff = abs(money_needed)
if input_line == 'ACTION':
    print(f'We are left with {diff:.2f} leva.')
elif money_needed < 0:
    print(f'We need {diff:.2f} leva for our actors.')
