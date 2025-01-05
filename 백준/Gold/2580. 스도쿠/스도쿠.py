# board = []

# while True:
#     try:
#         row = list(map(int, input().split(" ")))
#         board.append(row)
#     except:
#         break

# def check_row(y, value):
#     if value in board[y]:
#         return False
#     return True

# def check_column(x, value):
#     for i in range(len(board)):
#         if value == board[i][x]:
#             return False
#     return True

# def check_sec(y, x, value):
#     min_i, max_i = 0, 0
#     min_j, max_j = 0, 0
#     if y <= 2:
#         min_i, max_i = 0, 2
#     elif 2 < y <= 5:
#         min_i, max_i = 3, 5
#     elif 5 < y <= 8:
#         min_i, max_i = 6, 8
    
#     if x <= 2:
#         min_j, max_j = 0, 2
#     elif 2 < x <= 5:
#         min_j, max_j = 3, 5
#     elif 5 < x <= 8:
#         min_j, max_j = 6, 8
    
#     for i in range(min_i, max_i + 1):
#         for j in range(min_j, max_j + 1):
#             if board[i][j] == value:
#                 return False
#     return True   

# def find_value(y, x):
#     for i in range(1, 10):
#         if check_row(y, i) and check_column(x, i) and check_sec(y, x, i):
#             return i
#     return False

# stack = []
    
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         if board[i][j] == 0:           
#             stack.append((i, j))  
            

            

# 보드 입력받기
board = []

while True:
    try:
        row = list(map(int, input().split(" ")))
        board.append(row)
    except:
        break

# 행 체크
def check_row(y, value):
    if value in board[y]:
        return False
    return True

# 열 체크
def check_column(x, value):
    for i in range(len(board)):
        if value == board[i][x]:
            return False
    return True

# 3x3 섹션 체크
def check_sec(y, x, value):
    min_i, max_i = (y // 3) * 3, (y // 3) * 3 + 2
    min_j, max_j = (x // 3) * 3, (x // 3) * 3 + 2
    
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if board[i][j] == value:
                return False
    return True   

def solve_sudoku():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if check_row(i, num) and check_column(j, num) and check_sec(i, j, num):
                        board[i][j] = num  
                        if solve_sudoku(): 
                            return True
                        board[i][j] = 0 
                return False 
    return True 

solve_sudoku()
for row in board:
    print(" ".join(map(str, row)))


