T = int(input())
for _ in range(T):
    empty, full = list(map(int, input().split(" ")))
    coins_weight = full - empty
    coins = []
    N = int(input())
    for _ in range(N):
        value, weight = list(map(int, input().split(" ")))
        coins.append([value, weight])
    
    dp = [float('inf')] * (coins_weight + 1)#각 무게별 가치
    for value, weight in coins:
        if weight <= coins_weight:
            dp[weight] = min(dp[weight], value)
        for i in range(weight + 1, coins_weight + 1):
            prev_v = dp[i - weight]
            cur_v = dp[i]
            if cur_v == float('inf'):
                dp[i] = 0
            dp[i] = min(cur_v, prev_v + value)
    if dp[coins_weight] == float('inf'):
        print("This is impossible.")
    else:
        print(f"The minimum amount of money in the piggy-bank is {dp[coins_weight]}.")