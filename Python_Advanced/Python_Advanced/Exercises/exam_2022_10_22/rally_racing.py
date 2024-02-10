n = int(input())
tracked_car = input()

matrix = []
km = 0
position = [0, 0]
tunnel_pos = []
finished_race = False

for row in range(n):
    matrix.append([x for x in input().split()])
    if 'T' in matrix[row]:
        tunnel_pos.append([row, matrix[row].index('T')])

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

direction = input()
while direction != 'End':
    r, c = position[0] + directions[direction][0], position[1] + directions[direction][1]

    if matrix[r][c] == '.':
        km += 10
    elif matrix[r][c] == 'T':
        km += 30
        matrix[r][c] = '.'
        r, c = tunnel_pos[1][0], tunnel_pos[1][1]
        matrix[r][c] = '.'
    elif matrix[r][c] == 'F':
        position = [r, c]
        km += 10
        finished_race = True
        break

    position = [r, c]

    direction = input()

print(f"Racing car {tracked_car} finished the stage!" if finished_race
      else f"Racing car {tracked_car} DNF.")
print(f"Distance covered {km} km.")
matrix[position[0]][position[1]] = 'C'
[print(*row, sep='') for row in matrix]


# if the tunnels are on the same row
#
# n = int(input())
# tracked_car = input()
#
# matrix = []
# km = 0
# position = [0, 0]
# tunnel_pos = []
# finished_race = False
#
# for row in range(n):
#     matrix.append([x for x in input().split()])
#     if 'T' in matrix[row]:
#         if matrix[row].count('T') == 2:
#             for _ in range(2):
#                 tunnel_pos.append([row, matrix[row].index('T')])
#                 matrix[row][matrix[row].index('T')] = '.'
#         else:
#             tunnel_pos.append([row, matrix[row].index('T')])
#
# matrix[tunnel_pos[0][0]][tunnel_pos[0][1]] = 'T'
# matrix[tunnel_pos[1][0]][tunnel_pos[1][1]] = 'T'
# directions = {
#     'up': [-1, 0],
#     'down': [1, 0],
#     'left': [0, -1],
#     'right': [0, 1]
# }
#
# direction = input()
# while direction != 'End':
#     r, c = position[0] + directions[direction][0], position[1] + directions[direction][1]
#
#     if matrix[r][c] == '.':
#         km += 10
#     elif matrix[r][c] == 'T':
#         km += 30
#         matrix[r][c] = '.'
#         r, c = tunnel_pos[1][0], tunnel_pos[1][1]
#         matrix[r][c] = '.'
#     elif matrix[r][c] == 'F':
#         position = [r, c]
#         km += 10
#         finished_race = True
#         break
#
#     position = [r, c]
#
#     direction = input()
#
# print(f"Racing car {tracked_car} finished the stage!" if finished_race
#       else f"Racing car {tracked_car} DNF.")
# print(f"Distance covered {km} km.")
# matrix[position[0]][position[1]] = 'C'
# [print(*row, sep='') for row in matrix]
