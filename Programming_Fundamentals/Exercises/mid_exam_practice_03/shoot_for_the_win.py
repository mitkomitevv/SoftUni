list_targets = [int(x) for x in input().split()]
shot_targets = 0
for _ in range(len(list_targets)):
    input_line2 = input()
    if input_line2 == 'End':
        break
    target_index = int(input_line2)
    if target_index >= len(list_targets) or list_targets[target_index] == -1:
        continue
    value = list_targets[target_index]
    list_targets[target_index] = -1
    list_targets = [x if x == -1 else x + value if x <= value else x - value for x in list_targets]
    shot_targets = list_targets.count(-1)
print(f"Shot targets: {shot_targets} ->", *list_targets)
