filming_time = int(input())
scenes_number = int(input())
time_of_scenes = int(input())

terrain = filming_time * 0.15
total_scenes = scenes_number * time_of_scenes
total_filming = terrain + total_scenes

if total_filming > filming_time:
    time_needed = round(total_filming - filming_time)
    print(f"Time is up! To complete the movie you need {time_needed} minutes.")
else:
    time_left = round(filming_time - total_filming)
    print(f"You managed to finish the movie on time! You have {time_left} minutes left!")
