matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]
data = input().split()

all_directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 0)
)

for i in range(len(data)):
    row, col = [int(num) for num in data[i].split(',')]

    if matrix[row][col] > 0:
        for x, y in all_directions:
            r, c = row + x, col + y

            if 0 <= r < len(matrix) and 0 <= c < len(matrix):
                matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive = [n for row in range(len(matrix)) for n in matrix[row] if n > 0]
print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
[print(*row) for row in matrix]
