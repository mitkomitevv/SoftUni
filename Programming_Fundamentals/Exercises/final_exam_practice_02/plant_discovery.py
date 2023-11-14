def rate(dictionary, plant, rating):
    if plant in dictionary:
        dictionary[plant].append(rating)
        return dictionary
    return 'error'

def update(dictionary, plant, new_rarity):
    if plant in dictionary:
        dictionary[plant][0] = new_rarity
        return dictionary
    return 'error'

def reset(dictionary, plant):
    if plant in dictionary:
        dictionary[plant][1:] = ''
        return dictionary
    return 'error'

def printing(dictionary):
    print("Plants for the exhibition:")
    for key, value in dictionary.items():
        rarity = dictionary[key][0]
        rating = sum(dictionary[key][1:]) / len(dictionary[key][1:]) if len(dictionary[key][1:]) > 0 else 0
        print(f"- {key}; Rarity: {rarity}; Rating: {rating:.2f}")

def main():
    n = int(input())
    some_dict = {}
    for _ in range(n):
        plant, rarity = input().split('<->')
        if plant not in some_dict:
            some_dict[plant] = []
        some_dict[plant] += [rarity]

    input_line = input()
    while input_line != 'Exhibition':
        command, info = input_line.split(': ')
        info = ''.join(info).split(' - ')
        plant = info[0]
        if command == 'Rate':
            rating = int(info[1])
            result = rate(some_dict, plant, rating)
            if result == 'error':
                print('error')
            else:
                some_dict = result
        elif command == 'Update':
            new_rarity = int(info[1])
            result = update(some_dict, plant, new_rarity)
            if result == 'error':
                print('error')
            else:
                some_dict = result
        elif command == 'Reset':
            result = reset(some_dict, plant)
            if result == 'error':
                print('error')
            else:
                some_dict = result

        input_line = input()

    printing(some_dict)

if __name__ == '__main__':
    main()