number_of_groups = int(input())
musala, monblan, kilimanjaro, k2, everest = 0, 0, 0, 0, 0
total_people = 0

for _ in range(number_of_groups):
    current_group = int(input())
    total_people += current_group
    if current_group <= 5:
        musala += current_group
    elif 5 < current_group <= 12:
        monblan += current_group
    elif 12 < current_group <= 25:
        kilimanjaro += current_group
    elif 25 < current_group <= 40:
        k2 += current_group
    else:
        everest += current_group

musala_percentage = musala / total_people * 100
monblan_percentage = monblan / total_people * 100
kilimanjaro_percentage = kilimanjaro / total_people * 100
k2_percentage = k2 / total_people * 100
everest_percentage = everest / total_people * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')
