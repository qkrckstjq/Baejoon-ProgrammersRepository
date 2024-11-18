N, K = list(map(int, input().split(" ")))
stack = []
dp = [0] * (K + 1)
for _ in range(N):
    w, v = list(map(int, input().split(" ")))
    if w > K:
        continue
    stack.append([w, v])

for weight, value in stack:
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[K])