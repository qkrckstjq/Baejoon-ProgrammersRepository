N = int(input())
K = int(input())

low = 1
high = N * N

while low < high:
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, mid // i)
        
        if cnt >= K:
            break
    
    if cnt < K:
        low = mid + 1
    else:
        high = mid

print(low)