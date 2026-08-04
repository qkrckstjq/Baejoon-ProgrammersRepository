dy = [1, 1, -1, -1]
dx = [1, -1, 1, -1]
ud_y = [1, -1, 0, 0]
ud_x = [0, 0, 1, -1]
dy_2 = [2, -2, 0, 0]
dx_2 = [0, 0, 2, -2]


def solution(places):
    answer = []
    for i in range(len(places)):
        not_pass = False
        for y in range(len(places[i])):
            if not_pass:
                break
            for x in range(len(places[i][y])):
                if places[i][y][x] == "P" and not check_pass(y, x, places[i]):
                    not_pass = True
                    break
        if not_pass:
            answer.append(0)
        else:
            answer.append(1)
                
    return answer

def check_pass(y, x, board):
    global dy
    global dx
    global ud_y
    global ud_x
    global dy_2
    global dx_2
    max_y = len(board)
    max_x = len(board[0])
    
    for i in range(4):
        next_y = y + ud_y[i]
        next_x = x + ud_x[i]
        if next_y < 0 or next_y >= max_y or next_x < 0 or next_x >= max_x:
            continue
        if board[next_y][next_x] == "P":
            return False
        
    for i in range(4):
        next_y = y + dy_2[i]
        next_x = x + dx_2[i]
        if next_y < 0 or next_y >= max_y or next_x < 0 or next_x >= max_x:
            continue
        if board[next_y][next_x] != "P":
            continue
        next_y = next_y if next_y == y else (next_y - 1 if y < next_y else next_y + 1)
        next_x = next_x if next_x == x else (next_x - 1 if x < next_x else next_x + 1)
        if board[next_y][next_x] != "X":
            return False
        
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if next_y < 0 or next_y >= max_y or next_x < 0 or next_x >= max_x:
            continue
        if board[next_y][next_x] != "P":
            continue
        if board[next_y][x] != "X" or board[y][next_x] != "X":
            return False
        
    return True
        