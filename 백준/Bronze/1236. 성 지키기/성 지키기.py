N, M = map(int, input().split(" "))
board = []
for _ in range(N):
    row = list(input())
    board.append(row)

row = 0
col = 0

for i in range(N):
    empty = True
    for j in range(M):
        if board[i][j] == "X":
            empty = False
            break
    if empty:
        row += 1

for i in range(M):
    empty = True
    for j in range(N):
        if board[j][i] == "X":
            empty = False
            break
    if empty:
        col += 1

print(max(col, row))

