input_line = input()
contests = {}
while input_line != 'end of contests':
    contest, password = input_line.split(':')
    contests[contest] = password
    input_line = input()

input_line2 = input()
valid_contests = {}
while input_line2 != 'end of submissions':
    contest, password, username, points = input_line2.split('=>')
    points = int(points)
    list_with_contests = [contest, points]
    if contest in contests.keys():
        if password == contests[contest]:
            if username not in valid_contests:
                valid_contests[username] = {contest: points}
            else:
                if contest in valid_contests[username]:
                    if contest in valid_contests[username] and valid_contests[username][contest] < points:
                        valid_contests[username][contest] = points
                else:
                    valid_contests[username][contest] = points

    input_line2 = input()

best_candidate = 0
best_key = None  # Variable to store the key of the dictionary with the highest sum

for key, value_dict in valid_contests.items():
    max_candidate = sum(value_dict.values())
    if max_candidate > best_candidate:
        best_candidate = max_candidate
        best_key = key 

print(f"Best candidate is {best_key} with total {best_candidate} points.")


x = {'Tanya': {'C# Fundamentals': 350, 'Algorithms': 380, 'Part One Interview': 220, 'JS Fundamentals': 400}, 'Nikola': {'Part One Interview': 120, 'C# Fundamentals': 200}}