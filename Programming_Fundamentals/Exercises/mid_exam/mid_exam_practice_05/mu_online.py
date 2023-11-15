def potion(current_hp, hp_value):
    temp_health = current_hp
    current_hp += hp_value
    if current_hp > 100:
        current_hp = 100
    amount = current_hp - temp_health
    print(f"You healed for {amount} hp.\n"
          f"Current health: {current_hp} hp.")
    return current_hp

def chest(coins, found_coins):
    coins += found_coins
    print(f"You found {found_coins} bitcoins.")
    return coins

def fighting(hp, monster, attack, room, flag):
    hp -= attack
    if hp > 0:
        print(f"You slayed {monster}.")
    else:
        flag = True
        print(f"You died! Killed by {monster}.\n"
              f"Best room: {room}")
    return hp, flag

def last_print(health, bitcoins, dead):
    if not dead:
        print(f"You've made it!\n"
              f"Bitcoins: {bitcoins}\n"
              f"Health: {health}")

def main():
    input_line = input().split('|')
    health = 100
    bitcoins = 0
    room_number = 0
    dead = False
    for room in input_line:
        command, value = room.split()
        value = int(value)
        room_number += 1
        if command == 'potion':
            health = potion(health, value)
        elif command == 'chest':
            bitcoins = chest(bitcoins, value)
        else:
            health, dead = fighting(health, command, value, room_number, dead)
            if health <= 0:
                break
    return last_print(health, bitcoins, dead)
main()
