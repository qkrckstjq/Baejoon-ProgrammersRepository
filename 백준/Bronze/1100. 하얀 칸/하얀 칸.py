board = [list(input()) for _ in range(8)]

result = 0

for i in range(8):
    index = 0 if i % 2 == 0 else 1
    for j in range(index, 8, 2):
        if board[i][j] == "F":
            result += 1

print(result)