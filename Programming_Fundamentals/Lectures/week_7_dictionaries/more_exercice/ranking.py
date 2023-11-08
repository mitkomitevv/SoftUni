input_line = input()
contests = {}
while input_line != 'end of contests':
    contest, password = input_line.split(':')
    contests[contest] = password
    input_line = input()

input_line2 = input()
valid_contests = {}
list_with_contests = []
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



