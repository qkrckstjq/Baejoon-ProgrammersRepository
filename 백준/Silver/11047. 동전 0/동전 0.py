import sys


def s_input():
    return sys.stdin.readline().strip()


N, K = list(map(int, s_input().split(" ")))
coins = []
for i in range(N):
    coin = int(s_input())
    coins.append(coin)
count = 0
cur_value = 0
for i in range(len(coins) - 1, -1, -1):
    if coins[i] <= K:
        q = K // coins[i]
        count += q
        K -= q * coins[i]
    if K == 0:
        break
print(count)
