from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())
presents = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
flag = False

while materials and magic:
    curr_material = materials.pop()
    current_magic = magic.popleft()

    if curr_material == 0 or current_magic == 0:
        if curr_material == 0 and current_magic != 0:
            magic.appendleft(current_magic)
        elif current_magic == 0 and curr_material != 0:
            materials.append(curr_material)
        continue

    total_magic = curr_material * current_magic
    if total_magic == 150:
        presents['Doll'] += 1
    elif total_magic == 250:
        presents['Wooden train'] += 1
    elif total_magic == 300:
        presents['Teddy bear'] += 1
    elif total_magic == 400:
        presents['Bicycle'] += 1
    else:
        if total_magic < 0:
            materials.append(curr_material + current_magic)
        if total_magic > 0:
            materials.append(curr_material + 15)

print("The presents are crafted! Merry Christmas!" if presents['Doll'] > 0 and presents['Wooden train'] > 0
                                                      or presents['Teddy bear'] > 0 and presents['Bicycle'] > 0
                                                        else "No presents this Christmas!")
if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
sorted_presents = {k: presents[k] for k in sorted(presents)}
for present, count in sorted_presents.items():
    if count > 0:
        print(f"{present}: {count}")
