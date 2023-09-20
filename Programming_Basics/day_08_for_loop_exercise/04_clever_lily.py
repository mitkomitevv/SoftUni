age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys = 0
bd_money = 0
total_from_toys = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        bd_money = bd_money + int((i / 2) * 10 - 1)
    else:
        toys += 1
        total_from_toys = toys * toy_price

total_money = bd_money + total_from_toys
diff = abs(washing_machine_price - total_money)

if washing_machine_price <= total_money:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
