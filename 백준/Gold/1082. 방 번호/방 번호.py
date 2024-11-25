N = int(input())
costs = list(map(int, input().split(" ")))
money = int(input())

dp = [0] * (money + 1)

for i in range(len(costs)):
    num = len(costs) - 1 - i
    cost = costs[len(costs) - 1 - i]
    for j in range(cost, money + 1):
        dp[j] = max(dp[j], dp[j - cost]*10 + num)

print(dp[money])