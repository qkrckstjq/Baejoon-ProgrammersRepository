import sys
from collections import defaultdict


move_x = [0, 0, 1, -1, 1, -1, 1, -1]
move_y = [1, -1, 0, 0, 1, -1, -1, 1]

def s_input():
    return sys.stdin.readline().strip()

M, N = map(int, s_input().split(" "))

input_map = []
visit = defaultdict(dict)
check = defaultdict(dict)
result = 0

for i in range(M):
    x = list(map(int, s_input().split(" ")))
    input_map.append(x)
    
def check_range(cur_y, cur_x):
    return True if 0 <= cur_y < M and 0 <= cur_x < N else False

def check_dif(cur_v, next_v):
    dif = cur_v - next_v
    return True if 0 <= dif <= 1 else False

def check_visit(next_y, next_x):
    return True if not next_x in check[next_y] else False

def check_zero(next_y, next_x):
    return True if input_map[next_y][next_x] != 0 else False
    
def dfs(y, x):
    stack = [[y, x]]
    check[y][x] = True
    while stack:
        cur_y, cur_x = stack.pop()
        visit[cur_y][cur_x] = True
        cur_v = input_map[cur_y][cur_x]
        for i in range(8):
            next_y = cur_y + move_y[i]
            next_x = cur_x + move_x[i]
            next_v = 0
            
            if next_x in visit[next_y]:
                continue
            
            if not check_range(next_y, next_x):
                continue
            
            next_v = input_map[next_y][next_x]
            
            if cur_v < next_v:
                return 0
                
            if next_v == cur_v:
                visit[next_y][next_x] = True
                stack.append([next_y, next_x])
                check[next_y][next_x] = True
                
    return 1


for i in range(M):
    for j in range(N):
        if check_visit(i, j):
            visit = defaultdict(dict)
            result += dfs(i,j)
            
print(result)