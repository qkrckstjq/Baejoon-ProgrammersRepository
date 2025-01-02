N, M = map(int, input().split(" "))

bucket = [0 for _ in range(N + 1)]
for _ in range(M):
    i, j, k = list(map(int, input().split(" ")))
    for idx in range(i, j + 1):
        bucket[idx] = k

[print(bucket[i]) for i in range(1, len(bucket))]