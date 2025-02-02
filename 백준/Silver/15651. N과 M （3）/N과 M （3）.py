N, M = map(int, input().split(" "))
answer = []

def dfs(stack):
    if len(stack) == M:
        answer.append(" ".join(list(map(str, stack))))
        return
    
    for i in range(1, N + 1):
        stack.append(i)
        dfs(stack)
        stack.pop()
dfs([])
answer.sort()
for row in answer:
    print(row)