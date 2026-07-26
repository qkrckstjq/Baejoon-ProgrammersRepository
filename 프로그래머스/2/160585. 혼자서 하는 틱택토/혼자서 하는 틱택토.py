def solution(board):
    o = 0
    x = 0

    for row in board:
        o += row.count("O")
        x += row.count("X")

    if not (o == x or o == x + 1):
        return 0

    def is_win(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True

        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True
            
        if all(board[i][i] == player for i in range(3)):
            return True

        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    o_win = is_win("O")
    x_win = is_win("X")

    if o_win and x_win:
        return 0

    if o_win and o != x + 1:
        return 0

    if x_win and o != x:
        return 0

    return 1