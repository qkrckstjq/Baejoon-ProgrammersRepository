from collections import deque

R, C = map(int, input().split(" "))
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

board = []
r_y = 0
r_x = 0
b_y = 0
b_x = 0
for i in range(R):
    row = list(input())
    board.append(row)
    for j in range(len(row)):
        if row[j] == "R":
            r_y = i
            r_x = j
            board[i][j] = "."
        if row[j] == "B":
            b_y = i
            b_x = j
            board[i][j] = "."

queue = deque()
queue.append((r_y, r_x, b_y, b_x, 1))
visit = set([(r_y, r_x, b_y, b_x)])

def move(y, x, i):
    cnt = 0
    while board[y][x] != "O" and board[y][x] != "#":
        y += dy[i]
        x += dx[i]
        cnt += 1
    if board[y][x] == "O":
        return [y, x, cnt]
    if board[y][x] == "#":
        return [y - dy[i], x - dx[i], cnt]

find = False
while queue:
    cur_ry, cur_rx, cur_by, cur_bx, cur_k = queue.popleft()
    
    if find:
        break
    
    for i in range(4):
        next_ry, next_rx, r_cnt = move(cur_ry, cur_rx, i)
        next_by, next_bx, b_cnt = move(cur_by, cur_bx, i)
        
        if board[next_ry][next_rx] == "O" and board[next_by][next_bx] == "O":
            continue
            
        if board[next_ry][next_rx] == "O" and board[next_by][next_bx] != "O":
            find = True
            print(cur_k)
            break
        
        if next_ry == next_by and next_rx == next_bx:
            if r_cnt < b_cnt:
                next_by -= dy[i]
                next_bx -= dx[i]
            if r_cnt > b_cnt:
                next_ry -= dy[i]
                next_rx -= dx[i]
        
        if (next_ry, next_rx, next_by, next_bx) not in visit:
            queue.append((next_ry, next_rx, next_by, next_bx, cur_k + 1))
            visit.add((next_ry, next_rx, next_by, next_bx))
              
if not find:
    print(-1)