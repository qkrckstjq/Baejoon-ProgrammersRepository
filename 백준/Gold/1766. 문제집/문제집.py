import heapq
N, M = list(map(int, input().split(" "))) #정점 개수 N, 간선 개수 M

indegree = [0 for _ in range(N + 1)]
graph = {i : [] for i in range(1, N + 1)}

for _ in range(M):
    require, dst = list(map(int, input().split(" ")))
    graph[require].append(dst)
    indegree[dst] += 1

answer = []
queue = [i for i in range(1, N + 1) if indegree[i] == 0]
heapq.heapify(queue)
while queue:
    cur_node = heapq.heappop(queue)
    answer.append(cur_node)
    
    for dst_node in graph[cur_node]:
        indegree[dst_node] -= 1
        if indegree[dst_node] == 0:
            heapq.heappush(queue, dst_node)
            
print(" ".join(map(str, answer)))    