result = []
while True:
    target = int(input().strip())
    if target == 0:
        break

    if target <= 1:
        result.append(1)
        continue

    memo = [0] * (target + 1)
    memo[0] = memo[1] = 1

    for i in range(2, target + 1):
        memo[i] = memo[i - 1] + memo[i - 2]  # 직전과 그 이전의 경우의 수를 더합니다.

    result.append(memo[target])

for k in result:
    print(k)