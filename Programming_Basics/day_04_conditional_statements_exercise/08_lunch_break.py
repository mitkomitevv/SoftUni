import math

show_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
relax = break_length / 4
time_left = break_length - lunch_time - relax

diff = math.ceil(abs(time_left - episode_length))

if time_left >= episode_length:
    print(f"You have enough time to watch {show_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {diff} more minutes.")
