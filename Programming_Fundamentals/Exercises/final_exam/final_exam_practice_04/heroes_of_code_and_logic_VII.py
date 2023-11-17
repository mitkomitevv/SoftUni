def cast(heroes, hero_name, mp_needed, spell_name):
    if heroes[hero_name][1] >= mp_needed:
        heroes[hero_name][1] -= mp_needed
        return heroes, f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!"
    return heroes, f"{hero_name} does not have enough MP to cast {spell_name}!"

def damage(heroes, hero_name, damage_to_take, attacker):
    if heroes[hero_name][0] > damage_to_take:
        heroes[hero_name][0] -= damage_to_take
        return heroes, f"{hero_name} was hit for {damage_to_take} HP by {attacker} and now has {heroes[hero_name][0]} HP left!"
    del heroes[hero_name]
    return heroes, f"{hero_name} has been killed by {attacker}!"

def recharge(heroes, hero_name, amount):
    if heroes[hero_name][1] + amount > 200:
        recharged = 200 - heroes[hero_name][1]
        heroes[hero_name][1] = 200
        return heroes, f"{hero_name} recharged for {recharged} MP!"
    heroes[hero_name][1] += amount
    return heroes, f"{hero_name} recharged for {amount} MP!"

def heal(heroes, hero_name, amount):
    if heroes[hero_name][0] + amount > 100:
        healed = 100 - heroes[hero_name][0]
        heroes[hero_name][0] = 100
        return heroes, f"{hero_name} healed for {healed} HP!"
    heroes[hero_name][0] += amount
    return heroes, f"{hero_name} healed for {amount} HP!"

def main():
    num_heroes = int(input())
    heroes = {}
    for _ in range(num_heroes):
        input_line = input().split()
        hero, hp, mp = input_line[0], int(input_line[1]), int(input_line[2])
        if hp > 100:
            hp = 100
        if mp > 200:
            hp = 200
        if hero not in heroes:
            heroes[hero] = []
        heroes[hero] += [hp, mp]

    input_line = input()
    while input_line != 'End':
        input_line = input_line.split(' - ')
        command = input_line[0]
        if command == 'CastSpell':
            hero_name, mp_needed, spell_name = input_line[1], int(input_line[2]), input_line[3]
            heroes, message = cast(heroes, hero_name, mp_needed, spell_name)
            print(message)
        elif command == 'TakeDamage':
            hero_name, damage_to_take, attacker = input_line[1], int(input_line[2]), input_line[3]
            heroes, message = damage(heroes, hero_name, damage_to_take, attacker)
            print(message)
        elif command == 'Recharge':
            hero_name, amount = input_line[1], int(input_line[2])
            heroes, message = recharge(heroes, hero_name, amount)
            print(message)
        elif command == 'Heal':
            hero_name, amount = input_line[1], int(input_line[2])
            heroes, message = heal(heroes, hero_name, amount)
            print(message)

        input_line = input()

    for hero, values in heroes.items():
        print(f"{hero}\n"
              f"HP: {values[0]}\n"
              f"MP: {values[1]}")

if __name__ == '__main__':
    main()
