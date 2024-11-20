N, T = list(map(int, input().split(" ")))
delay_amount = []
total_amount = 0
for _ in range(N):
    delay, amount = list(map(int, input().split(" ")))
    delay_amount.append([delay, amount])
    total_amount += amount
dp = [0] * (T + 1)
for delay, amount in delay_amount:
    for i in range(T, delay - 1, -1):
        dp[i] = max(dp[i], dp[i - delay] + amount)

print(total_amount - dp[T])