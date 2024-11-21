N, K = list(map(int, input().split(" ")))
caffeines = list(map(int, input().split(" ")))
dp = [float('inf')] * (K + 1)
dp[0] = 0
for c in caffeines:
    if c <= K:
        dp[c] = 1
    for i in range(K, c - 1, -1):
        dp[i] = min(dp[i], dp[i - c] + 1) 
if dp[K] == float('inf'):
    print(-1)
else:
    print(dp[K])