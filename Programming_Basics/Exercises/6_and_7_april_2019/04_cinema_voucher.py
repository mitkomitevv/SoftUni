voucher = int(input())
total_money = 0
price = 0
flag = False
movie_counter = 0
product_counter = 0

product = input()
while product != 'End':
    money_left = abs(voucher - total_money)
    if len(product) > 8:
        first_letter = product[:1]
        second_letter = product[1:2]
        price = ord(first_letter) + ord(second_letter)
        movie_counter += 1
        if price > money_left:
            movie_counter -= 1
            flag = True
            break
    elif len(product) <= 8:
        first_letter = product[:1]
        price = ord(first_letter)
        product_counter += 1
        if price > money_left:
            product_counter -= 1
            flag = True
            break

    total_money += price
    # money_left = abs(voucher - total_money)

    # if price > money_left:
    #     flag = True
    #     break

    product = input()


print(movie_counter)
print(product_counter)


