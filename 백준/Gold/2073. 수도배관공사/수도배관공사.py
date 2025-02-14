D, P = map(int, input().split(" "))
pipes = []
for _ in range(P):
    L, C = map(int, input().split(" "))
    pipes.append((L, C))

dp = [0] * (D + 1)  # 0으로 초기화 (아무것도 사용하지 않은 상태)

# DP 업데이트 (배낭 문제와 유사하게 뒤에서부터 진행)
for L, C in pipes:
    for i in range(D, L - 1, -1):  # 뒤에서부터 순회 (중복 방지)
        if dp[i - L] > 0 or i == L:  # i-L이 0보다 크다면 만들 수 있는 상태임
            dp[i] = max(dp[i], min(dp[i - L], C) if dp[i - L] > 0 else C)

# 정답 출력
print(dp[D])
