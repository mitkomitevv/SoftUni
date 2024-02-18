from collections import deque

elfs_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
toys_made, energy_used, turn = 0, 0, 0


while elfs_energy and materials:
    elf = elfs_energy.popleft()

    if elf < 5:
        continue
    turn += 1
    material = materials.pop()

    if turn % 3 == 0:
        if elf >= material * 2:
            toys_made += 2
            current_elf = elf - (material * 2) + 1
            if turn % 5 == 0:
                toys_made -= 2
                current_elf -= 1
            energy_used += material * 2
            elfs_energy.append(current_elf)
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)

    elif turn % 5 == 0:
        if elf >= material:
            energy_used += material
            elfs_energy.append(elf - material)
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)

    else:
        if elf >= material:
            toys_made += 1
            energy_used += material
            elfs_energy.append(elf - material + 1)
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)

print(f"Toys: {toys_made}")
print(f"Energy: {energy_used}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
