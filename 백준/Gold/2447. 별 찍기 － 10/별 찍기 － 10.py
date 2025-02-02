N = int(input())

grid = [[" " for _ in range(N)] for _ in range(N)]

def recursion(y, x, cur):
    if cur == 1:
        grid[y][x] = "*"
        return
    next_cur = cur // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            recursion(y + i * next_cur, x + j * next_cur, next_cur)

recursion(0, 0, N)
# print(grid)
for row in grid:
    print("".join(row))