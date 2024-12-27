from collections import deque

def solution(board):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    sy, sx = 0, 0
    ey, ex = 0, 0
    
    def check_range(y, x):
        return 0 <= y < len(board) and 0 <= x < len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                sy, sx = i, j
            if board[i][j] == "G":
                ey, ex = i, j
    
    queue = deque()
    queue.append((sy, sx, 0))
    visit = set()
    visit.add((sy, sx))
    
    while queue:
        cur_y, cur_x, cur_k = queue.popleft()
        if cur_y == ey and cur_x == ex:
            return cur_k
        for i in range(4):
            next_y, next_x = cur_y, cur_x
            while True:
                next_y += dy[i]
                next_x += dx[i]
                if not check_range(next_y, next_x) or board[next_y][next_x] == "D":
                    next_y -= dy[i]
                    next_x -= dx[i]
                    break
            if (next_y, next_x) not in visit:
                queue.append((next_y, next_x, cur_k + 1))
                visit.add((next_y, next_x))
    
    return -1
