import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]  # -1로 초기화 (아직 탐색되지 않은 값)

def dfs(y, x):
    if y == N - 1 and x == M - 1:  # 도착점 도달 시 경로 1개 찾음
        return 1
    
    if dp[y][x] != -1:  # 이미 계산된 경우 반환 (중복 호출 방지)
        return dp[y][x]
    
    dp[y][x] = 0  # 탐색 시작 (현재 노드에서 가능한 경로 수 0으로 초기화)
    cur_val = grid[y][x]
    
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < N and 0 <= next_x < M:
            if cur_val > grid[next_y][next_x]:  # 내리막길 탐색
                dp[y][x] += dfs(next_y, next_x)  # 가능한 경로 수 누적
    
    return dp[y][x]

print(dfs(0, 0))
