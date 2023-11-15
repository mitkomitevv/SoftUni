def loot(chest_contents, looting):
    for x in looting:
        if x not in chest_contents:
            chest_contents.insert(0, x)
    return chest_contents

def drop(chest_contents, dropped_index):
    if dropped_index < len(chest_contents):
        popped = chest_contents.pop(dropped_index)
        chest_contents.append(popped)
    return chest_contents

def steal(chest_contents, count):
    stolen = chest_contents[-count:]
    del chest_contents[-count:]
    print(f"{', '.join(stolen)}")
    return chest_contents

def main():
    initial_loot = input().split('|')
    input_line = input().split()
    while input_line[0] != 'Yohoho!':
        command = input_line[0]
        if command == 'Loot':
            initial_loot = loot(initial_loot, input_line[1:])
        elif command == 'Drop':
            initial_loot = drop(initial_loot, int(input_line[1]))
        elif command == 'Steal':
            initial_loot = steal(initial_loot, int(input_line[1]))
        input_line = input().split()
    if initial_loot:
        total = sum(len(item) for item in initial_loot)
        count = len(initial_loot)
        average_gain = total / count
        return f"Average treasure gain: {average_gain:.2f} pirate credits."
    else:
        return f"Failed treasure hunt."
print(main())
