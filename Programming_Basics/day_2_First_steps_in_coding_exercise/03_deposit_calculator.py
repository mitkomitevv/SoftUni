deposit_amount = float(input())
months = int(input())
annual_rate = float(input())

rate = deposit_amount * (annual_rate / 100)
rate_for_a_month = rate / 12

total_sum = deposit_amount + months * rate_for_a_month

print(total_sum)