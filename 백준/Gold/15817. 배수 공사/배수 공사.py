N, X = map(int, input().split(" "))
pipes = []
dp = [0 for _ in range(X + 1)]
dp[0] = 1
for _ in range(N):
    L, C = map(int, input().split(" "))
    pipes.append((L, C))

for L, C in pipes:
    for i in range(X, -1, -1):
        for j in range(1, C + 1):
            if i - L * j >= 0:
                dp[i] += dp[i - L * j]
            else:
                break

print(dp[-1])