N, M = map(int, input().split(" "))
bytes = list(map(int, input().split(" ")))
costs = list(map(int, input().split(" ")))

# 비용의 최대 합계를 계산
max_cost = sum(costs)
dp = [0] * (max_cost + 1)  # 비용별로 확보할 수 있는 최대 바이트 수 기록

for i in range(N):
    byte = bytes[i]
    cost = costs[i]
    for j in range(max_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + byte)

# 최소 비용을 찾음
result = min(cost for cost, mem in enumerate(dp) if mem >= M)
print(result)
