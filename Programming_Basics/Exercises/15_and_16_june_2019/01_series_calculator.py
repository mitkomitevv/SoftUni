from math import floor

tv_series = input()
seasons_number = int(input())
episodes_number = int(input())
runtime_without_ads = float(input())

ads_per_episode = runtime_without_ads * 0.2
runtime_total = runtime_without_ads + ads_per_episode
total_extra_time = seasons_number * 10

total = floor(runtime_total * episodes_number * seasons_number + total_extra_time)

print(f"Total time needed to watch the {tv_series} series is {total} minutes.")
