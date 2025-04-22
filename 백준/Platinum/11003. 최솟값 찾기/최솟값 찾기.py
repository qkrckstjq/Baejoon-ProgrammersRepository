from collections import deque

N, L = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

dq = deque()
result = []

# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6

for i in range(N):
    while dq and dq[-1][1] > A[i]:
        dq.pop()
    
    dq.append((i, A[i]))

    if dq[0][0] <= i - L:
        dq.popleft()
    
    result.append(dq[0][1])

print(' '.join(map(str, result)))
