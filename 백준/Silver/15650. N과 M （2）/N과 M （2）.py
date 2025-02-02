N, M = map(int, input().split(" "))

answer = []

def dfs(stack):
    if len(stack) == M:
        answer.append(" ".join(list(map(str, stack))))
        return
    start = 1 if not stack else (stack[-1] + 1)
    for i in range(start, N + 1):
        stack.append(i)
        dfs(stack)
        stack.pop()

dfs([])

for row in answer:
    print(row)