def get_dst(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

T = int(input())

for i in range(T):
    x1, y1, x2, y2 = list(map(int, input().split(" ")))
    w = int(input())
    count = 0
    for j in range(w):
        x, y, v = list(map(int, input().split(" ")))
        dst1 = get_dst(x, y, x1, y1)
        dst2 = get_dst(x, y, x2, y2)
        if (dst1 < v) != (dst2 < v):
            count += 1
    print(count)