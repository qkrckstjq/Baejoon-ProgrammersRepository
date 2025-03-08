from collections import deque
N = int(input())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
board = [list(map(int, input().split(" "))) for _ in range(N)]
min_len = float('inf')
index_island = [[False for _ in range(N)] for _ in range(N)]

def dfs(y, x, idx):
    stack = [(y, x)]
    visit = set()
    while stack:
        cur_y, cur_x = stack.pop()
        index_island[cur_y][cur_x] = idx
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0 <= next_y < N and 0 <= next_x < N:
                if (next_y, next_x) not in visit and board[next_y][next_x] == 1:
                    visit.add((next_y, next_x))
                    stack.append((next_y, next_x))
                    
def bfs(y, x, cur_idx):
    visit = set([(y, x)])
    queue = deque()
    
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < N and 0 <= next_x < N and board[next_y][next_x] == 0:
            queue.append((next_y, next_x, 1))
    
    while queue:
        cur_y, cur_x, cur_len = queue.popleft()
        if cur_len > min_len:
            return min_len
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            next_len = cur_len + 1
            if 0 <= next_y < N and 0 <= next_x < N:
                if (next_y, next_x) not in visit and index_island[next_y][next_x] != cur_idx:
                    if board[next_y][next_x] == 1:
                        # print(y, x, next_y, next_x, cur_len)
                        return cur_len
                    visit.add((next_y, next_x))
                    queue.append((next_y, next_x, next_len))
    return float('inf')
                    
idx = 1
for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            if index_island[y][x] == False:
                dfs(y, x, idx)
                idx += 1
            min_len = min(bfs(y, x, index_island[y][x]), min_len) 

print(min_len)