import heapq
N, M = map(int, input().split(" "))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

grid = []
for _ in range(N):
    row = list(map(int, input().split(" ")))
    grid.append(row)

def find_land(y, x, i):
    result = 0
    while (0 <= y < N and 0 <= x < M) and grid[y][x] == 0:
        result += 1
        y += dy[i]
        x += dx[i]
    
    if (0 <= y < N and 0 <= x < M):
        return result
    else:
        False

def re_color(y, x, i, visit):
    stack = [(y, x)]
    visit[y][x] = True
    # visit = set([(y, x)])
    while stack:
        cur_y, cur_x = stack.pop()
        grid[cur_y][cur_x] = i
        for j in range(4):
            next_y = cur_y + dy[j]
            next_x = cur_x + dx[j]
            if (0 <= next_y < N and 0 <= next_x < M) and not visit[next_y][next_x] and grid[next_y][next_x] != 0:
                stack.append((next_y, next_x))
                visit[next_y][next_x] = True
                
color_num = 1
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0 and not visit[i][j]:
            re_color(i, j, color_num, visit)
            color_num += 1
# [print(" ".join(list(map(str, row)))) for row in grid]
graph = {i : {} for i in range(1, color_num)}

def find(y, x, cur_node):
    stack = []
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < N and 0 <= next_x < M:
            if grid[next_y][next_x] == 0:
                stack.append(i)
    # print(f"{y}, {x}일때 이동 가능한 방향 {stack}")
    for i in stack:
        next_y = y + dy[i]
        next_x = x + dx[i]
        cnt = 0
        while 0 <= next_y < N and 0 <= next_x < M and grid[next_y][next_x] == 0:
            next_y += dy[i]
            next_x += dx[i]
            cnt += 1
        if 0 <= next_y < N and 0 <= next_x < M:
            dst = grid[next_y][next_x]
            if dst != 0 and cnt >= 2:
                if dst in graph[cur_node]:
                    graph[cur_node][dst] = min(cnt, graph[cur_node][dst])
                else:
                    graph[cur_node][dst] = cnt
                
                if cur_node in graph[dst]:
                    graph[dst][cur_node] = min(cnt, graph[dst][cur_node])
                else:
                    graph[dst][cur_node] = cnt
                    
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0:
            # print((i, j))
            find(i, j, grid[i][j])

# print("\n")
# [print(" ".join(list(map(str, row)))) for row in grid]
# print(graph)

queue = []
visit = set()
answer = 0
for i in range(1, color_num):
    if list(graph[i].items()):
        heapq.heappush(queue, (0, i))
        break
cnt = 0
while queue:
    cur_value, cur_node = heapq.heappop(queue)
    if cur_node in visit:
        continue
    visit.add(cur_node)
    cnt += 1
    answer += cur_value
    if cnt == (color_num - 1):
        break
    for dst, value in graph[cur_node].items():
        if dst not in visit:
            heapq.heappush(queue, (value, dst))

if cnt != (color_num - 1):
    print(-1)
else:
    print(answer)