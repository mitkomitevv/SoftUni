def enough_chairs(num):
    free_chairs = 0
    flag = False
    for n in range(1, num + 1):
        string = input().split()
        chairs = len(string[0])
        visitors = int(string[1])
        if visitors > chairs:
            flag = True
            needed_chairs = visitors - chairs
            print(f'{needed_chairs} more chairs needed in room {n}')
        else:
            free_chairs += chairs - visitors
    if not flag:
        print(f'Game On, {free_chairs} free chairs left')


number_of_rooms = int(input())
enough_chairs(number_of_rooms)
