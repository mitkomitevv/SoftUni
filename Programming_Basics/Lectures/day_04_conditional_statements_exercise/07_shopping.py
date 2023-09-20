budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

price_gpu = gpu_count * 250
price_cpu = cpu_count * (price_gpu * 0.35)
price_ram = ram_count * (price_gpu * 0.1)

total = price_gpu + price_cpu + price_ram

if gpu_count > cpu_count:
    total = total * 0.85

diff = abs(budget - total)

if budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")