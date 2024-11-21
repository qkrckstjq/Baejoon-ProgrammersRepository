N, Q = list(map(int, input().split(" ")))
bytes = list(map(int, input().split(" ")))
costs = list(map(int, input().split(" ")))
M = sum(costs)
dp = [0] * (M + 1)
for i in range(N):
    byte = bytes[i]
    cost = costs[i]
    for j in range(M, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + byte)
print(min([cost for cost in range(M + 1) if dp[cost] >= Q]))
