def main():
    houses = [int(x) for x in input().split('@')]
    command = input()
    house_number = 0
    while command != 'Love!':
        command = command.split()
        idx = int(command[1])
        house_number += idx
        if house_number > len(houses) - 1:
            house_number = 0
        jumping(houses ,house_number)
        command = input()
    return printing(houses, house_number)

def jumping(houses, current_house):
    if houses[current_house] == 0:
        print(f"Place {current_house} already had Valentine's day.")
    elif houses[current_house] >= 2:
        houses[current_house] -= 2
        if houses[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")

def printing(houses, current_house):
    print(f"Cupid's last position was {current_house}.")
    if len(houses) == houses.count(0):
        print("Mission was successful.")
    else:
        zeroes = houses.count(0)
        count = len(houses) - zeroes
        print(f"Cupid has failed {count} places.")

main()
