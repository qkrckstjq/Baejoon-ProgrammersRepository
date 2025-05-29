N = int(input())
board = []

for i in range(N):
    y, x = map(int, input().split(" "))
    board.append((y, x))

answer = 0
for i in range(len(board)):
    y1, x1 = board[i]
    y2, x2 = board[(i + 1) % N]
    answer += (y1 * x2) - (x1 * y2)

print(round(abs(answer) / 2, 2))