board = []

for _ in range(9):
    row = list(map(int, list(input()))) 
    board.append(row)

def check_y(x, num):
    for i in range(9):
        if board[i][x] == num:
            return False
    return True

def check_x(y, num):
    for i in range(9):
        if board[y][i] == num:
            return False
    return True

def check_sec(y, x, num):
    y_range = (y // 3) * 3
    x_range = (x // 3) * 3
    # print(y_range * 3, y_range * 3 + 3)
    # print(x_range * 3, x_range * 3 + 3)
    for i in range(y_range, y_range + 3):
        for j in range(x_range, x_range + 3):
            if board[i][j] == num:
                return False
    return True

def dfs():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if check_y(j, num) and check_x(i, num) and check_sec(i, j, num):
                        board[i][j] = num
                        if dfs():
                            return True
                        board[i][j] = 0
                return False
    return True #False라면 완성되었다는것

dfs()

[print("".join(list(map(str, row)))) for row in board]