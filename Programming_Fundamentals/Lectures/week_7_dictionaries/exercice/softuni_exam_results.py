first_line = input().split('-')
results = {}
submissions = {}
while 'exam finished' not in first_line:
    name = first_line[0]
    if 'banned' in first_line:
        del results[name]
        first_line = input().split('-')
        continue
    language = first_line[1]
    points = int(first_line[2])

    if name not in results.keys():
        results[name] = points
    elif results[name] < points:
        results[name] = points

    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1
    first_line = input().split('-')

print('Results:')
for name, points in results.items():
    print(f"{name} | {points}")
print('Submissions:')
for language, count in submissions.items():
    print(f'{language} - {count}')
