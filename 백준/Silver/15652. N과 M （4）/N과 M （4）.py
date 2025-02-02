N, M = map(int, input().split(" "))
answer = []

def dfs(stack):
    if len(stack) == M:
        answer.append(" ".join(list(map(str, stack))))
        return
    start = stack[-1] if stack else 1
    for i in range(start, N + 1):
        stack.append(i)
        dfs(stack)
        stack.pop()

dfs([])
answer.sort()
for row in answer:
    print(row)