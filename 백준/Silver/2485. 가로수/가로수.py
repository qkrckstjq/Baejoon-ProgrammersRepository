N = int(input())

def uclid(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

grid = []
for _ in range(N):
    grid.append(int(input()))

cur = uclid(grid[2] - grid[1], grid[1] - grid[0])
for i in range(3, len(grid)):
    cur = uclid(cur, grid[i] - grid[i - 1])

print(((grid[-1] - grid[0]) // cur) - N + 1)