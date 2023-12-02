def plundering(cities, town, people, gold):
    cities[town][0] -= people
    cities[town][1] -= gold
    if cities[town][0] == 0 or cities[town][1] == 0:
        print(f"{town} has been wiped off the map!")
        del cities[town]
    return cities

def prospering(cities, town, gold):
    if gold < 0:
        return cities, "Gold added cannot be a negative number!"
    cities[town][1] += gold
    return cities, f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold."

def printing(cities):
    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for town, pop_gold in cities.items():
            print(f"{town} -> Population: {pop_gold[0]} citizens, Gold: {pop_gold[1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")

def main():
    line = input().split('||')
    cities = {}
    while line[0] != 'Sail':
        city, population, gold = line[0], int(line[1]), int(line[2])
        if city not in cities:
            cities[city] = [0, 0]
        cities[city][0] += population
        cities[city][1] += gold

        line = input().split('||')

    line2 = input().split('=>')
    while line2[0] != 'End':
        command, town = line2[0], line2[1]
        if command == 'Plunder':
            people, gold = int(line2[2]), int(line2[3])
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities = plundering(cities, town, people, gold)
        elif command == 'Prosper':
            gold = int(line2[2])
            cities, message = prospering(cities, town, gold)
            print(message)

        line2 = input().split('=>')

    printing(cities)

if __name__ == '__main__':
    main()
