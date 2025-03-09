from collections import deque

# 입력 받기 (세로, 가로)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 시작과 끝 좌표 및 방향 (좌표는 0-index로 변환)
s_y, s_x, s_d = map(int, input().split())
e_y, e_x, e_d = map(int, input().split())
s_y, s_x, e_y, e_x = s_y - 1, s_x - 1, e_y - 1, e_x - 1

# 회전 명령: 문제 명세에 따른 좌/우 회전 결과
turn = {
    1: [4, 3],
    2: [3, 4],
    3: [1, 2],
    4: [2, 1]
}

# 이동 방향: 1: 동, 2: 서, 3: 남, 4: 북
dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]

# 방문 처리: visited[y][x][d]
visited = [[[False] * 5 for _ in range(M)] for _ in range(N)]

# 초기 상태 큐에 넣기 전에 방문 처리
queue = deque()
queue.append((s_y, s_x, s_d, 0))
visited[s_y][s_x][s_d] = True

while queue:
    y, x, d, cnt = queue.popleft()
    if y == e_y and x == e_x and d == e_d:
        print(cnt)
        break

    # 회전 명령 (좌회전, 우회전)
    for nd in turn[d]:
        if not visited[y][x][nd]:
            visited[y][x][nd] = True
            queue.append((y, x, nd, cnt + 1))

    # 이동 명령 (Go 1, 2, 3)
    ny, nx = y, x
    for k in range(1, 4):
        ny += dy[d]
        nx += dx[d]
        if not (0 <= ny < N and 0 <= nx < M) or board[ny][nx] == 1:
            break
        if not visited[ny][nx][d]:
            visited[ny][nx][d] = True
            queue.append((ny, nx, d, cnt + 1))
