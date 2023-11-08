collected = {'shards': 0, 'fragments': 0, "motes": 0}
legendary_item = ''
found = False
while True:
    materials = input().split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()
        if material not in collected:
            collected[material] = 0
        collected[material] += quantity

        if collected[material] >= 250:
            if material == 'shards':
                found = True
                legendary_item = 'Shadowmourne'
            elif material == 'fragments':
                found = True
                legendary_item = 'Valanyr'
            elif material == 'motes':
                found = True
                legendary_item = 'Dragonwrath'

        if found:
            collected[material] -= 250
            break
    if found:
        break

print(f'{legendary_item} obtained!')
for material, quantity in collected.items():
    print(f"{material}: {quantity}")



# collected = {}
# legendary_item = ''
# found = False
# while True:
#     materials = input().split()
#     for i in range(0, len(materials), 2):
#         quantity = int(materials[i])
#         material = materials[i + 1].lower()
#         if material not in collected:
#             collected[material] = 0
#         collected[material] += quantity
#
#         if collected[material] >= 250:
#             if material == 'shards':
#                 found = True
#                 legendary_item = 'Shadowmourne'
#             elif material == 'fragments':
#                 found = True
#                 legendary_item = 'Valanyr'
#             elif material == 'motes':
#                 found = True
#                 legendary_item = 'Dragonwrath'
#
#         if found:
#             collected[material] -= 250
#             break
#     if found:
#         break
#
# print(f'{legendary_item} obtained!')
# print(f"shards: {collected.get('shards') if collected.get('shards') is not None else 0}")
# print(f"fragments: {collected.get('fragments') if collected.get('fragments') is not None else 0}")
# print(f"motes: {collected.get('motes') if collected.get('motes') is not None else 0}")
# for key, value in collected.items():
#     if key != 'shards' and key != 'fragments' and key != 'motes':
#         print(f"{key}: {value}")


