actor_name = input()
academy_points = float(input())
appraisers_number = int(input())
points = 0
total_points = 0

for _ in range(appraisers_number):
    name_appraiser = input()
    points_appraiser = float(input())
    length = len(name_appraiser)
    points += (length * points_appraiser) / 2
    total_points = points + academy_points

    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break
else:
    diff = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
