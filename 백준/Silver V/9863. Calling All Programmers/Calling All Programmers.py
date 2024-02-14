while True:
# count = 0
    n, m, k = map(int, input().split())
    queue = []

    for i in range(n):
        queue.append(i+1)

    if n == 0 and m == 0 and k == 0: # 10 7 5
        break
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10
    for i in range(k): # 0 ~ 4
        for j in range(m-1): # 0 ~ 6
            queue.append(queue.pop(0))

        if i == k-1:
            print(queue.pop(0))
# count = 0
            break
        queue.pop(0)