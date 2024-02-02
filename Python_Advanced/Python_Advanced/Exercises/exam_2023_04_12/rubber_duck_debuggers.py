from collections import deque

time = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

ducks_given = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time and tasks:
    curr_time, task = time.popleft(), tasks.pop()
    result = curr_time * task

    if 0 <= result <= 60:
        ducks_given["Darth Vader Ducky"] += 1
    elif 60 < result <= 120:
        ducks_given["Thor Ducky"] += 1
    elif 120 < result <= 180:
        ducks_given["Big Blue Rubber Ducky"] += 1
    elif 180 < result <= 240:
        ducks_given["Small Yellow Rubber Ducky"] += 1
    else:
        time.append(curr_time)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{k}: {v}") for k,v in ducks_given.items()]
