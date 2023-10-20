def fire(ship, idx, dmg, valid_index):
    if 0 <= idx < len(ship):
        valid_index = True
        ship[idx] -= dmg
    else:
        valid_index = False
    return ship, valid_index

def defend(ship, idx1, idx2, dmg):
    if 0 <= idx1 < len(ship) and 0 <= idx2 < len(ship):
        ship = [x-dmg if idx1 <= i < idx2 + 1 else x for i, x in enumerate(ship)]
    return ship

def repair(ship, idx, hp, max_hp):
    if 0 <= idx < len(ship):
        ship[idx] += hp
        if ship[idx] > max_hp:
            ship[idx] = max_hp
    return ship

def status(ship, max_hp):
    for_repair = 0
    for section in ship:
        if section < max_hp * 0.2:
            for_repair += 1
    return for_repair

def main():
    pirate_ship = [int(x) for x in input().split('>')]
    warship = [int(x) for x in input().split('>')]
    max_sect_hp = int(input())
    command = input()
    valid_index = False
    pirate_dead = False
    warship_dead = False
    while command != 'Retire':
        command = command.split()
        if 'Fire' in command:
            index, damage = int(command[1]), int(command[2])
            warship, valid_index = fire(warship, index, damage, valid_index)
            if valid_index:
                if warship[index] <= 0:
                    warship_dead = True
                    print('You won! The enemy ship has sunken.')
                    break

        elif 'Defend' in command:
            start_idx, end_idx, damage = int(command[1]), int(command[2]), int(command[3])
            pirate_ship = defend(pirate_ship, start_idx, end_idx, damage)
            for hp in pirate_ship:
                if hp <= 0:
                    pirate_dead = True

        elif 'Repair' in command:
            index, health = int(command[1]), int(command[2])
            pirate_ship = repair(pirate_ship, index, health, max_sect_hp)

        elif 'Status' in command:
            count_repair = status(pirate_ship, max_sect_hp)
            print(f'{count_repair} sections need repair.')

        command = input()

    if not pirate_dead and not warship_dead:
        print(f"Pirate ship status: {sum(pirate_ship)}\n"
              f"Warship status: {sum(warship)}")

    elif pirate_dead:
        print('You lost! The pirate ship has sunken.')

    return warship
main()
