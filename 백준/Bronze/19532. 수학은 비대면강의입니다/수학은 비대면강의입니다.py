x, y, c, x1, y1, f = map(int, input().split(" "))

for i in range(-999, 1000):
    find = False
    answer_x = None
    answer_y = None
    for j in range(-999, 1000):
        if ((x * i) + (y * j) == c) and ((x1 * i) + (y1 * j) == f):
            answer_x, answer_y = i, j
            find = True
    if find:
        print(answer_x, answer_y)
        break