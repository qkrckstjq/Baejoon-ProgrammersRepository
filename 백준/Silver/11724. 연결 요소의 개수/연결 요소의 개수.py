N, M = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    src, dst = map(int, input().split(" "))
    graph[src].append(dst)
    graph[dst].append(src)
visit = [False for _ in range(N + 1)]

answer = 0
for node in range(1, N + 1):
    if visit[node]:
        continue
    stack = [node]
    while stack:
        cur_node = stack.pop()
        
        for next_node in graph[cur_node]:
            if not visit[next_node]:
                stack.append(next_node)
                visit[next_node] = True
    
    answer += 1

print(answer)