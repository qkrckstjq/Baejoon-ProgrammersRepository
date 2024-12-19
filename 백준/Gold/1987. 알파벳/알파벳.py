import copy

R, C = map(int, input().split(" "))
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def check_range(y, x):
    return True if 0 <= y < R and 0 <= x < C else False

board = []

for _ in range(R):
    row = list(input())
    board.append(row)

result = 0
visit = set([board[0][0]])
def dfs(y, x, k):
    global result
    result = max(result, k)
    next_k = k + 1
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if check_range(next_y, next_x):
            next_word = board[next_y][next_x]        
            if next_word not in visit:
                visit.add(next_word)
                dfs(next_y, next_x, next_k)
                visit.remove(next_word)

dfs(0, 0, 1)

print(result)