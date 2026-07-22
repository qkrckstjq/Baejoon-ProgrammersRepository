def solution(n):
    board = [[0] * n for _ in range(n)]

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x = -1
    y = 0
    num = 1
    direction = 0

    for length in range(n, 0, -1):
        for _ in range(length):
            x += dx[direction]
            y += dy[direction]
            board[x][y] = num
            num += 1

        direction = (direction + 1) % 3

    answer = []

    for i in range(n):
        for j in range(i + 1):
            answer.append(board[i][j])

    return answer