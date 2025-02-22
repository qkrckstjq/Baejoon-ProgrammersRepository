N = int(input())
board = []
for _ in range(N):
    row = list(map(int, input().split(" ")))
    board.append(row)

blue = 0
white = 0

def recursion(y1, y2, x1, x2):
    global board, blue, white
    prev = None
    same = True
    for y in range(y1, y2):
        if not same:
            break
        for x in range(x1, x2):
            if prev == None:
                prev = board[y][x]
                continue
            if prev != board[y][x]:
                if not same:
                    break
                same = False
                mid_y = (y1 + y2) // 2
                mid_x = (x1 + x2) // 2
                
                recursion(y1, mid_y, x1, mid_x)
                recursion(y1, mid_y, mid_x, x2)
                recursion(mid_y, y2, x1, mid_x)
                recursion(mid_y, y2, mid_x, x2)
                
    if same:
        if prev == 0:
            white += 1
            # print(f"y = ({y1} ~ {y2}) x = ({x1} ~ {x2}) 이 범위는 모두 흰색임")
        else:
            blue += 1
            # print(f"y = ({y1} ~ {y2}) x = ({x1} ~ {x2}) 이 범위는 모두 파란색")

recursion(0, N, 0, N)
print(white)
print(blue)