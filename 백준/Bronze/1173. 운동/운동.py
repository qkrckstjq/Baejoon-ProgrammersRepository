N, m, M, T, R = list(map(int, input().split(" ")))

time = 0
start = m
ex = 0
rest = False

while ex < N:
    if start + T <= M:
        start += T
        ex += 1
        rest = False
    elif start - R >= m:
        start -= R
        rest = False
    else:
        if rest:
            print(-1)
            break
        start = m
        rest = True
    time += 1
else:
    print(time)
        