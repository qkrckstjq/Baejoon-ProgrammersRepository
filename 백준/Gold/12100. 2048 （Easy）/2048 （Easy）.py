import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 네 방향: 아래, 위, 오른쪽, 왼쪽
def move(b, d):
    if d == 0:  # 아래
        for x in range(N):
            for y in range(N-2, -1, -1):
                if b[y][x]:
                    ny = y
                    while ny+1 < N and b[ny+1][x] == 0:
                        ny += 1
                    if ny != y:
                        b[ny][x], b[y][x] = b[y][x], 0
    if d == 1:  # 위
        for x in range(N):
            for y in range(1, N):
                if b[y][x]:
                    ny = y
                    while ny-1 >= 0 and b[ny-1][x] == 0:
                        ny -= 1
                    if ny != y:
                        b[ny][x], b[y][x] = b[y][x], 0
    if d == 2:  # 오른쪽
        for y in range(N):
            for x in range(N-2, -1, -1):
                if b[y][x]:
                    nx = x
                    while nx+1 < N and b[y][nx+1] == 0:
                        nx += 1
                    if nx != x:
                        b[y][nx], b[y][x] = b[y][x], 0
    if d == 3:  # 왼쪽
        for y in range(N):
            for x in range(1, N):
                if b[y][x]:
                    nx = x
                    while nx-1 >= 0 and b[y][nx-1] == 0:
                        nx -= 1
                    if nx != x:
                        b[y][nx], b[y][x] = b[y][x], 0

def merge(b, d):
    merged_any = False
    if d in (0, 1):
        for x in range(N):
            merged = [False]*N
            if d == 0:
                for y in range(N-1, 0, -1):
                    if b[y][x] and b[y][x] == b[y-1][x] and not merged[y] and not merged[y-1]:
                        b[y][x] *= 2
                        b[y-1][x] = 0
                        merged[y] = True
                        merged_any = True
            else:
                for y in range(N-1):
                    if b[y][x] and b[y][x] == b[y+1][x] and not merged[y] and not merged[y+1]:
                        b[y][x] *= 2
                        b[y+1][x] = 0
                        merged[y] = True
                        merged_any = True
    else:
        for y in range(N):
            merged = [False]*N
            if d == 2:
                for x in range(N-1, 0, -1):
                    if b[y][x] and b[y][x] == b[y][x-1] and not merged[x] and not merged[x-1]:
                        b[y][x] *= 2
                        b[y][x-1] = 0
                        merged[x] = True
                        merged_any = True
            else:
                for x in range(N-1):
                    if b[y][x] and b[y][x] == b[y][x+1] and not merged[x] and not merged[x+1]:
                        b[y][x] *= 2
                        b[y][x+1] = 0
                        merged[x] = True
                        merged_any = True
    return merged_any

def copy_board(b):
    return [row[:] for row in b]

def dfs(b, depth):
    global result
    # 매 노드마다 최대값 갱신
    for row in b:
        result = max(result, max(row))
    if depth == 5:
        return

    for d in range(4):
        nb = copy_board(b)
        move(nb, d)
        merged = merge(nb, d)
        move(nb, d)
        # 실제 변화가 있을 때만 이동 1회로 간주
        if merged or nb != b:
            dfs(nb, depth+1)

# 특수 케이스
if N == 1:
    print(board[0][0])
    sys.exit()

dfs(board, 0)
print(result)
