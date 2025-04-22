from collections import deque

R, C = map(int, input().split(" "))
board = [list(input()) for _ in range(R)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

s_y, s_x = 0, 0
fire_queue = deque()
fire_visit = [[False for _ in range(C)] for _ in range(R)]
s_find, f_find = False, False
for y in range(R):
    for x in range(C):
        if board[y][x] == "J":
            s_y, s_x = y, x
        if board[y][x] == "F":
            fire_queue.append((y, x))
            fire_visit[y][x] = True
        
        if s_find and f_find:
            break

def fire():
    for _ in range(len(fire_queue)):
        y, x = fire_queue.popleft()
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if 0 <= next_y < R and 0 <= next_x < C:
                if not fire_visit[next_y][next_x] and board[next_y][next_x] != "#":
                    fire_visit[next_y][next_x] = True
                    fire_queue.append((next_y, next_x))
                    board[next_y][next_x] = "F"
        
queue = deque()
queue.append((s_y, s_x, 0, 0))
cnt = 0

visit = [[False for _ in range(C)] for _ in range(R)]
visit[s_y][s_x] = True
find = False
while queue and not find:
    cur_y, cur_x, cur_k, cur_cnt = queue.popleft()
    
    if cnt == cur_cnt:
        fire()
        cnt += 1
    
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if 0 <= next_y < R and 0 <= next_x < C:
            if not visit[next_y][next_x] and board[next_y][next_x] == ".":
                visit[next_y][next_x] = True
                queue.append((next_y, next_x, cur_k + 1, cur_cnt + 1))
        else:
            print(cur_k + 1)
            find = True
            break
        
if not find:
    print("IMPOSSIBLE")