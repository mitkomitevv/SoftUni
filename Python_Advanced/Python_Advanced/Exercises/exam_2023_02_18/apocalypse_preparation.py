from collections import deque

textiles = deque(int(x) for x in input().split())
medications = deque(int(x) for x in input().split())

cost = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

healing_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medications:
    textile = textiles.popleft()
    medication = medications.pop()
    result = textile + medication

    for item, value in cost.items():
        if result == value:
            healing_items[item] += 1
            break
    else:
        if result > 100:
            healing_items["MedKit"] += 1
            medications[-1] += result - 100
        else:
            medications.append(medication + 10)

if not textiles and not medications:
    print("Textiles and medicaments are both empty.")
elif not medications:
    print("Medicaments are empty.")
else:
    print("Textiles are empty.")

healing_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))
[print(f"{item_name} - {amount_created}") for item_name, amount_created in healing_items if amount_created > 0]
if medications:
    medications.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medications)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")



# from collections import deque
#
# textiles = deque(int(x) for x in input().split())
# medications = deque(int(x) for x in input().split())
#
# healing_items = {
#     "Patch": 0,
#     "Bandage": 0,
#     "MedKit": 0
# }
#
# while True:
#
#     if not textiles and not medications:
#         print("Textiles and medicaments are both empty.")
#         break
#     if not medications:
#         print("Medicaments are empty.")
#         break
#     if not textiles:
#         print("Textiles are empty.")
#         break
#
#     textile = textiles.popleft()
#     medication = medications.pop()
#     result = textile + medication
#
#     if result == 30:
#         healing_items["Patch"] += 1
#     elif result == 40:
#         healing_items["Bandage"] += 1
#     elif result == 100:
#         healing_items["MedKit"] += 1
#     elif result > 100:
#         healing_items["MedKit"] += 1
#         medications[-1] += result - 100
#     else:
#         medications.append(medication + 10)
#
# sorted_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))
# [print(f"{item_name} - {amount_created}") for item_name, amount_created in sorted_items if amount_created > 0]
# if medications:
#     medications.reverse()
#     print(f"Medicaments left: {', '.join(str(x) for x in medications)}")
# if textiles:
#     print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
