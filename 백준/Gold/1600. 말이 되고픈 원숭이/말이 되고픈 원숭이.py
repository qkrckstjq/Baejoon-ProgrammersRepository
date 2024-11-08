from collections import deque

K = int(input())
W, H = map(int, input().split())
input_map = [list(map(int, input().split())) for _ in range(H)]

hx = [2, 2, -2, -2, -1, -1, 1, 1]
hy = [1, -1, 1, -1, 2, -2, -2, 2]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

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
    
    if not visit[cur_y][cur_x][cur_k]:
        visit[cur_y][cur_x][cur_k] = True
        
        if cur_k > 0:
            next_k = cur_k - 1
            for i in range(8):
                next_y, next_x = cur_y + hy[i], cur_x + hx[i]
                if 0 <= next_y < H and 0 <= next_x < W and input_map[next_y][next_x] == 0 and not visit[next_y][next_x][next_k]:
                    queue.append((next_y, next_x, next_k, cur_move + 1))
        
        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= next_y < H and 0 <= next_x < W and input_map[next_y][next_x] == 0 and not visit[next_y][next_x][cur_k]:
                queue.append((next_y, next_x, cur_k, cur_move + 1))

if not find:
    print(-1)
