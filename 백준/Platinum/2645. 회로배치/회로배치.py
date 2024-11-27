import heapq, copy
n = int(input())
y1, x1, y2, x2 = list(map(int, input().split(" ")))
k = int(input())
m = int(input())
grid = [[False for _ in range(n + 1)] for _ in range(n + 1)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def check(y1, x1, y2, x2, grid):
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                grid[y1][i] = True
        else:
            for i in range(x1, x2 - 1, -1):
                grid[y1][i] = True
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                grid[i][x1] = True
        else:
            for i in range(y1, y2 - 1, -1):
                grid[i][x1] = True
                
def check_range(y, x):
    return True if 1 <= y <= n and 1 <= x <= n else False

for _ in range(m):
    input_grid = list(map(int, input().split(" ")))
    for i in range(1, len(input_grid) - 3, 2):
        check(input_grid[i], input_grid[i + 1], input_grid[i + 2], input_grid[i + 3], grid)
    
min_heap = []
heapq.heappush(min_heap, (k if grid[y1][x1] else 1, y1, x1, f"{y1} {x1}", -1))
visit = set()
visit.add((y1, x1))

while min_heap:
    cur_v, cur_y, cur_x, route, d = heapq.heappop(min_heap)
    if cur_y == y2 and cur_x == x2:
        route += f" {cur_y} {cur_x}"
        coords = route.split()
        print(cur_v)
        print(len(coords) // 2, route)
        break

    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        next_d = i
        if check_range(next_y, next_x) and (next_y, next_x) not in visit:
            new_route = route
            if d != -1 and next_d != d:
                new_route += f" {cur_y} {cur_x}"
            next_v = cur_v + (k if grid[next_y][next_x] else 1)
            heapq.heappush(min_heap, (next_v, next_y, next_x, new_route, next_d))
            visit.add((next_y, next_x))
