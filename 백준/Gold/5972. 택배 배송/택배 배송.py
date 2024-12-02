import heapq
N, M = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}

for _ in range(M):
    src, dst, v = map(int, input().split(" "))
    graph[src].append((dst, v))
    graph[dst].append((src, v))

d = [float('inf') for _ in range(N + 1)]
queue = []
heapq.heappush(queue, (0, 1))

while queue:
    cur_v, cur_src = heapq.heappop(queue)
    if d[cur_src] < cur_v:
        continue
    for next_src, next_v in graph[cur_src]:
        total_v = cur_v + next_v
        if d[next_src] > total_v:
            d[next_src] = total_v
            heapq.heappush(queue, (total_v, next_src))

print(d[N])