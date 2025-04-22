from collections import deque

R, C = map(int, input().split(" "))
board = []

def print_board():
    for y in range(R):
        print("".join(board[y]))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(R):
    row = list(input())
    board.append(row)
    
s_y, s_x = 0, 0
for y in range(R):
    for x in range(C):
        if board[y][x] == "S":
            s_y, s_x = y, x
            break
    
def water():
    stack = []
    for y in range(R):
        for x in range(C):
            if board[y][x] == "*":
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if 0 <= next_y < R and 0 <= next_x < C:
                        if board[next_y][next_x] != "D" and board[next_y][next_x] != "X":
                            stack.append((next_y, next_x))
                            
    for y, x in stack:
        board[y][x] = "*"
        
queue = deque()
queue.append((s_y, s_x, 0, 0))

visit = [[False for _ in range(C)] for _ in range(R)]

cnt = 0
find = False
while queue:
    cur_y, cur_x, cur_k, cur_cnt = queue.popleft()
    if board[cur_y][cur_x] == "D":
        print(cur_k)
        find = True
        break
    if cur_cnt == cnt:
        water()
        cnt += 1
    
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if 0 <= next_y < R and 0 <= next_x < C:
            if not visit[next_y][next_x] and board[next_y][next_x] != "*" and board[next_y][next_x] != "X":
                visit[next_y][next_x] = True
                queue.append((next_y, next_x, cur_k + 1, cur_cnt + 1))

if not find:
    print("KAKTUS")