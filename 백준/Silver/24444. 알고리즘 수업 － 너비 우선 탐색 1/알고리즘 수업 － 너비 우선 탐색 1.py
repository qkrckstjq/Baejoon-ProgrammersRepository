from collections import deque
N, M, R = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    src, dst = map(int, input().split(" "))
    graph[src].append(dst)
    graph[dst].append(src)
for i in range(1, N + 1):
    graph[i].sort()
answer = [0 for _ in range(N + 1)]
queue = deque()
queue.append(R)
cnt = 1
visit = [False for _ in range(N + 1)]
visit[R] = True
while queue:
    cur_node = queue.popleft()
    answer[cur_node] = cnt
    cnt += 1
    for next_node in graph[cur_node]:
        if not visit[next_node]:
            visit[next_node] = True
            queue.append(next_node)

[print(answer[i]) for i in range(1, N + 1)]

