from collections import deque

N, M = map(int, input().split(" "))
indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    require, dst = map(int, input().split(" "))
    indegree[dst] += 1
    graph[require].append(dst)

# print(graph)

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    cur_node = queue.popleft()
    result.append(cur_node)
    for next_node in graph[cur_node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            # print(f"{next_node}는 임계차수 0")
            queue.append(next_node)
            
print(" ".join(list(map(str, result))))