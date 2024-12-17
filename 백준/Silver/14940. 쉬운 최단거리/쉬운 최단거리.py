from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
N, M = map(int, input().split())

board = []
start_y, start_x = -1, -1

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if board[i][j] == 2:
            start_y, start_x = i, j

dist = [[-1] * M for _ in range(N)]
dist[start_y][start_x] = 0

queue = deque()
queue.append((start_y, start_x))

while queue:
    cur_y, cur_x = queue.popleft()
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if 0 <= next_y < N and 0 <= next_x < M:
            if board[next_y][next_x] != 0 and dist[next_y][next_x] == -1:
                dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                queue.append((next_y, next_x))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
