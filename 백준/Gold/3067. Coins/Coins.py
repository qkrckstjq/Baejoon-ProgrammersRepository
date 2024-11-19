T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split(" ")))
    target = int(input())
    dp = [0] * (target + 1)
    for coin in coins:
        dp[coin] += 1
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    print(dp[target])
    