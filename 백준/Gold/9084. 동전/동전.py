T = int(input())

result = []
for _ in range(T):
    var = int(input())
    coins = list(map(int, input().split(" ")))
    target = int(input())
    dp = [0] * (target + 1)
    for coin in coins:
        if coin <= target:
            dp[coin] += 1
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    result.append(dp[target])
[print(num) for num in result]