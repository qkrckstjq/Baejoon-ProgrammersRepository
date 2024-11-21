N, Q = list(map(int, input().split(" ")))
bytes = list(map(int, input().split(" ")))
costs = list(map(int, input().split(" ")))
M = sum(bytes)
dp = [float('inf')] * (M + 1)
dp[0] = 0
result = float('inf')
for i in range(N):
    byte = bytes[i]
    cost = costs[i]
    for j in range(M, byte - 1, -1):
        dp[j] = min(dp[j], dp[j - byte] + cost)
        if j >= Q:
            result = min(result, dp[j])
print(result)
