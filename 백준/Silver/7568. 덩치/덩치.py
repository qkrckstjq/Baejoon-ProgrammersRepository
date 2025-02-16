N = int(input())
ranks = [list(map(int, input().split(" "))) for _ in range(N)]
answer = [0 for _ in range(N)]
for i in range(N):
    rank = 0
    for j in range(N):
        if i == j:
            continue
        if ranks[i][0] < ranks[j][0] and ranks[i][1] < ranks[j][1]:
            rank += 1
    answer[i] = rank + 1

print(" ".join(list(map(str, answer))))
