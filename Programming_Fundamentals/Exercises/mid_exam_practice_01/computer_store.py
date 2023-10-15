price_without_tax = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price < 0:
        print('Invalid price!')
        continue
    price_without_tax += price
taxes = price_without_tax * 0.20
total_price = price_without_tax + taxes

if command == 'special':
    total_price = total_price * 0.9
if price_without_tax == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_tax:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")