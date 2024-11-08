from collections import deque

K = int(input())
W, H = map(int, input().split())
input_map = [list(map(int, input().split())) for _ in range(H)]

hx = [2, 2, -2, -2, -1, -1, 1, 1]
hy = [1, -1, 1, -1, 2, -2, -2, 2]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_move(y, x):
    return True if input_map[y][x] == 0 else False

def check_range(y, x):
    return True if 0 <= y < len(input_map) and 0 <= x < len(input_map[0]) else False

def check_visit(y, x, k, visit):
    return True if not visit[y][x][k] else False

queue = deque()
visit = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
queue.append((0, 0, K, 0))
find = False

while queue:
    cur_y, cur_x, cur_k, cur_move = queue.popleft()
    
    if cur_y == H - 1 and cur_x == W - 1:
        print(cur_move)
        find = True
        break
    
    if not visit[cur_y][cur_x][cur_k]:  # 방문 여부 체크 후 표시
        visit[cur_y][cur_x][cur_k] = True

        if cur_k > 0:
            next_k = cur_k - 1
            for i in range(8):
                next_y, next_x = cur_y + hy[i], cur_x + hx[i]
                if check_range(next_y, next_x) and check_move(next_y, next_x) and check_visit(next_y, next_x, next_k, visit):
                    queue.append((next_y, next_x, next_k, cur_move + 1))

        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if check_range(next_y, next_x) and check_move(next_y, next_x) and check_visit(next_y, next_x, cur_k, visit):
                queue.append((next_y, next_x, cur_k, cur_move + 1))

if not find:
    print(-1)
