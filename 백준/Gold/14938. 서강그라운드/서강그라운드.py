import heapq
N, M, R = map(int, input().split(" "))
points = list(map(int, input().split(" ")))
graph = {i : {} for i in range(1, N + 1)}

for _ in range(R):
    src, dst, w = map(int, input().split(" "))
    graph[src][dst] = w
    graph[dst][src] = w

max_point = 0
for node in range(1, N + 1):
    queue = []
    heapq.heappush(queue, (0, node))
    visit = [False for _ in range(N + 1)]
    result = 0
    while queue:
        cur_len, cur_node = heapq.heappop(queue)
        result += 0 if visit[cur_node] else points[cur_node - 1]
        visit[cur_node] = True
        for next_node in graph[cur_node]:
            total_len = cur_len + graph[cur_node][next_node]
            if total_len <= M:
                heapq.heappush(queue, (total_len, next_node))
    max_point = max(max_point, result)

print(max_point)
            