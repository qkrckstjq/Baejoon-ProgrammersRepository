from collections import deque

r, c = list(map(int, input().split(" ")))
maze = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for _ in range(r):
    column = list(map(int, input()))
    maze.append(column)

def check_range(y, x):
    return True if 0 <= y < r and 0 <= x < c else False

queue = deque([[0, 0, 0]])
visit = set()
while queue:
    cur_y, cur_x, cnt = queue.popleft()
    if (cur_y, cur_x) in visit:
        continue
    visit.add((cur_y, cur_x))
    if cur_y == r - 1 and cur_x == c - 1:
        print(cnt + 1)
        break
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if check_range(next_y, next_x) and maze[next_y][next_x] == 1:
            queue.append([next_y, next_x, cnt + 1])