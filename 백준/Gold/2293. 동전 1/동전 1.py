N, K = map(int, input().split(" "))
coins = [int(input()) for _ in range(N)]
dp = [0 for _ in range(K + 1)]

for coin in coins:
    if coin <= K:
        dp[coin] += 1
        for i in range(coin, K + 1):
            dp[i] += dp[i - coin]

print(dp[K])