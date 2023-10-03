number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    needed_capsules = int(input())

    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= needed_capsules <= 2000:
        price = capsule_price * days * needed_capsules
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')
