N, M = map(int, input().split(" "))
memo = {}
for _ in range(N):
    word = input()
    if len(word) >= M:
        if word in memo:
            memo[word] += 1
        else:
            memo[word] = 1

answer = list(memo.keys())
answer.sort(key=lambda x:(-memo[x], -len(x), x))
[print(word) for word in answer]