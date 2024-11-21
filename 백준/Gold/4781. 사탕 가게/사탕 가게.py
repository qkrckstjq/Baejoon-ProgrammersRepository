result = []
while True:
    # 입력 처리
    num, money = map(float, input().split())
    if num == 0 and money == 0.00:
        break

    # 소수점 두 자리까지 반올림하여 정수 변환
    max_money = int(money * 100 + 0.5)
    dp = [0] * (max_money + 1)

    # 각 음식의 칼로리(cal)와 비용(cost) 입력
    for _ in range(int(num)):
        cal, cost = map(float, input().split())
        cost = int(cost * 100 + 0.5)  # 소수점 두 자리까지 반올림하여 정수 변환
        for i in range(cost, max_money + 1):
            dp[i] = max(dp[i], dp[i - cost] + int(cal))

    # 최대 칼로리 결과 저장
    result.append(dp[max_money])

# 출력
for cal in result:
    print(int(cal))
