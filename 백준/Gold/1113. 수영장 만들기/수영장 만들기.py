N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def dfs_fill(sy, sx):
    stack = [(sy, sx)]
    visited = [[False]*M for _ in range(N)]
    visited[sy][sx] = True
    
    mini_pool = [(sy, sx)]
    start_h = board[sy][sx]
    min_h = 10
    
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                return 0
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if board[ny][nx] <= start_h:
                    stack.append((ny, nx))
                    mini_pool.append((ny, nx))
                else:
                    min_h = min(min_h, board[ny][nx])
    
    fill = min_h - start_h
    if fill <= 0:
        return 0
    
    water = 0
    for (y, x) in mini_pool:
        water += min_h - board[y][x]
        board[y][x] = min_h
    
    return water

for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] < 9:
            answer += dfs_fill(i, j)

print(answer)
