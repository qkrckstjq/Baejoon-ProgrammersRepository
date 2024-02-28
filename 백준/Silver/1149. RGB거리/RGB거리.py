import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
max_d = 987654321
memo = [[max_d]*3 for _ in range(N)]
rgb_info = []
for i in range(N):
    rgb = list(map(int, s_input().split(" ")))
    rgb_info.append(rgb)
for i in range(3):
    memo[0][i] = rgb_info[0][i]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            next_v = rgb_info[i][k] + memo[i - 1][j]
            if memo[i][k] > next_v:
                memo[i][k] = next_v

print(min(memo[N - 1]))