from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 1) 시작점과 초기 불 프론티어 준비
s_y = s_x = 0
fire_stack = deque()
fire_visit = [[False]*C for _ in range(R)]

for y in range(R):
    for x in range(C):
        if board[y][x] == 'J':
            s_y, s_x = y, x
            board[y][x] = '.'           # 출발 지점은 빈 칸으로
        elif board[y][x] == 'F':
            fire_stack.append((y, x))
            fire_visit[y][x] = True     # 초기 불 위치 방문 표시

def fire():
    # 현재 프론티어 크기만큼만 처리
    for _ in range(len(fire_stack)):
        y, x = fire_stack.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if not fire_visit[ny][nx] and board[ny][nx] == '.':
                    fire_visit[ny][nx] = True
                    board[ny][nx] = 'F'
                    fire_stack.append((ny, nx))

def print_board():
    for row in board:
        print(''.join(row))

# 2) 지훈이 BFS
queue = deque()
queue.append((s_y, s_x, 0, 0))  # y, x, k(탈출시간), cnt(타임스텝)
visit = [[False]*C for _ in range(R)]
visit[s_y][s_x] = True

cnt = 0
escaped = False

while queue and not escaped:
    y, x, k, t = queue.popleft()

    # 한 타임(초)이 바뀔 때마다 불 전파
    if t == cnt:
        fire()
        cnt += 1

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        # 보드 밖으로 나가면 탈출
        if not (0 <= ny < R and 0 <= nx < C):
            print(k + 1)
            escaped = True
            break

        # 다음 칸이 빈 칸(.)이어야만 이동
        if not visit[ny][nx] and board[ny][nx] == '.':
            visit[ny][nx] = True
            queue.append((ny, nx, k + 1, t + 1))

if not escaped:
    print("IMPOSSIBLE")
