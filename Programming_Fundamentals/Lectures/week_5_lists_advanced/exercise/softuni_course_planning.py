initial_schedule = input().split(', ')
schedule = initial_schedule.copy()
line2 = input()
while line2 != 'course start':
    command = line2.split(':')
    if 'Add' in command:
        if command[1] not in schedule:
            schedule.append(command[1])
    elif 'Insert' in command:
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])
    elif 'Remove' in command:
        if command[1] in schedule:
            schedule.remove(command[1])
            if f'{command[1]}-Exercise' in schedule:
                schedule.remove(f'{command[1]}-Exercise')
    elif 'Swap' in command:
        if command[1] in schedule and command[2] in schedule:
            lesson1_i = schedule.index(command[1])
            lesson2_i = schedule.index(command[2])
            schedule[lesson1_i], schedule[lesson2_i] = schedule[lesson2_i], schedule[lesson1_i]
            if f'{command[1]}-Exercise' in schedule:
                for_insert = schedule.index(command[1])
                schedule.remove(f'{command[1]}-Exercise')
                schedule.insert(for_insert, f'{command[1]}-Exercise')
            elif f'{command[2]}-Exercise' in schedule:
                for_insert = schedule.index(command[2])
                schedule.remove(f'{command[2]}-Exercise')
                schedule.insert(for_insert + 1, f'{command[2]}-Exercise')
    elif 'Exercise' in command:
        if command[1] in schedule and 'Exercise' not in schedule:
            lesson_i = schedule.index(command[1])
            schedule.insert(lesson_i + 1, f'{command[1]}-Exercise')
        else:
            schedule.append(command[1])
            schedule.append(f'{command[1]}-Exercise')
    line2 = input()
for i, lesson in enumerate(schedule, start=1):
    print(f'{i}.{lesson}')
