N, K = list(map(int, input().split(" ")))
lectures = []
dp = [0] * (N + 1)
for _ in range(K):
    K, T = list(map(int, input().split(" ")))
    lectures.append((K, T))

for k, t in lectures:
    for i in range(N, t - 1, -1):
        dp[i] = max(dp[i], dp[i - t] + k)

print(dp[N])