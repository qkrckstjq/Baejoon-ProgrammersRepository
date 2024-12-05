N = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

grid = []
for _ in range(N):
    grid.append(list(input()))

def check_range(y, x):
    return True if 0 <= y < N and 0 <= x < N else False

def dfs(start_y, start_x, grid, visit, type):
    colors = []
    start_color = grid[start_y][start_x]
    if type and (start_color == "G" or start_color == "R"):
        colors = ['G', 'R']
    elif not type and start_color != 'B':
        colors = [start_color]
    else:
        colors = ['B']
    # print(f"{'기본' if not type else '적녹색약'} 좌표y : {start_y}, 좌표x : {start_x}, 허용색들 : {colors}")
    stack = [(start_y, start_x)]
    visit.add((start_y, start_x))
    while stack:
        cur_y, cur_x = stack.pop()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if check_range(next_y, next_x):
                next_color = grid[next_y][next_x]
                if (next_y, next_x) not in visit and next_color in colors:
                    stack.append((next_y, next_x))
                    visit.add((next_y, next_x))

result_a = 0
result_b = 0

visit_a = set() #기본
visit_b = set() #적녹색약
for y in range(N):
    for x in range(N):
        if (y, x) not in visit_a:
            dfs(y, x, grid, visit_a, False)
            result_a += 1
        if (y, x) not in visit_b:
            dfs(y, x, grid, visit_b, True)
            result_b += 1

print(result_a, result_b)