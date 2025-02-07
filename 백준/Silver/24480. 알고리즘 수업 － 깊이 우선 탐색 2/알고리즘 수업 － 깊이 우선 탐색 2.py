from collections import deque
N, M, start = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}

for _ in range(M):
    src, dst = map(int, input().split(" "))
    graph[src].append(dst)
    graph[dst].append(src)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

# print(graph)

cnt = 1
answer = [0 for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

stack = [start]

while stack:
    # print(stack, visit)
    cur_node = stack.pop()
    
    if not visit[cur_node]:
        visit[cur_node] = True        
        answer[cur_node] = cnt
        cnt += 1

        for next_node in reversed(graph[cur_node]):
            if not visit[next_node]:
                stack.append(next_node)

[print(answer[i]) for i in range(1, N + 1)]