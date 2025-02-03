N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

max_sum = -float('inf')
cur = 0
for i in range(M):
    cur += arr[i]
max_sum = max(max_sum, cur)
start = 0
for i in range(M, N):
    cur = cur + arr[i] - arr[start]
    max_sum = max(max_sum, cur)
    start += 1

print(max_sum)