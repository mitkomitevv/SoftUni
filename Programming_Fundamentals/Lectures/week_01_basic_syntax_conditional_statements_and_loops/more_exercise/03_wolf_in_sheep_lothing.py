string = input()
my_list = [word.strip() for word in string.split(',')]
reversed_list = my_list[::-1]
wolf_position = reversed_list.index('wolf')
for i in range(len(reversed_list)):
    if wolf_position == 0:
        print('Please go away and stop eating my sheep')
        break
    else:
        print(f'Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!')
        break
