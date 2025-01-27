from collections import deque

R, C = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

grid = [list(input()) for _ in range(R)]

def bfs(y, x):
    queue = deque([(y, x, 0)])  # (y, x, 거리)
    visit = set([(y, x)])
    max_distance = 0

    while queue:
        cur_y, cur_x, cur_dist = queue.popleft()
        max_distance = max(max_distance, cur_dist)
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0 <= next_y < R and 0 <= next_x < C and (next_y, next_x) not in visit and grid[next_y][next_x] == "L":
                visit.add((next_y, next_x))
                queue.append((next_y, next_x, cur_dist + 1))

    return max_distance

# 모든 육지에서 BFS 수행
answer = 0
for y in range(R):
    for x in range(C):
        if grid[y][x] == "L":
            answer = max(answer, bfs(y, x))

print(answer)
