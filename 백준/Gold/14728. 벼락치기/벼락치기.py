def max_score_optimized(N, T, chapters):
    # DP 배열 초기화
    dp = [0] * (T + 1)
    
    # 각 단원에 대해 DP 갱신
    for time, value in chapters:
        for j in range(T, time - 1, -1):  # 뒤에서부터 순회
            dp[j] = max(dp[j], dp[j - time] + value)
    
    return dp[T]

N, T = list(map(int, input().split(" ")))
chapters = []
for _ in range(N):
    time, value = list(map(int, input().split(" ")))
    chapters.append([time, value])

print(max_score_optimized(N, T, chapters))