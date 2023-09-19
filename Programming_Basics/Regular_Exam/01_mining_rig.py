import math

price_gpu = int(input())
adapter = int(input())
gpu_electricity_per_day_price = float(input())
profit_from_gpu_per_day = float(input())

all_gpu_price = price_gpu * 13
all_adapter_price = adapter * 13
total_money_spend = all_adapter_price + all_gpu_price + 1000
gpu_for_day = profit_from_gpu_per_day - gpu_electricity_per_day_price
total_gpu_profit = gpu_for_day * 13
days_needed_to_turn_profit = math.ceil(total_money_spend / total_gpu_profit)

print(total_money_spend)
print(days_needed_to_turn_profit)
