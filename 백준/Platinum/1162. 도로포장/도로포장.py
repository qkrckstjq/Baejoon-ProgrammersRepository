import heapq

N, M, K = map(int, input().split(" "))
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    src, dst, w = map(int, input().split())
    graph[src].append((dst, w))
    graph[dst].append((src, w))

d = [[float('inf') for _ in range(K + 1)] for _ in range(N + 1)]

queue = []
heapq.heappush(queue, (0, 1, 0))
d[1][0] = 0

while queue:
    cur_v, cur_src, cur_k = heapq.heappop(queue)

    if cur_v > d[cur_src][cur_k]:
        continue

    for next_src, next_v in graph[cur_src]:
        total_v = next_v + cur_v

        if d[next_src][cur_k] > total_v:
            d[next_src][cur_k] = total_v
            heapq.heappush(queue, (total_v, next_src, cur_k))

        if cur_k < K and d[next_src][cur_k + 1] > cur_v:
            d[next_src][cur_k + 1] = cur_v
            heapq.heappush(queue, (cur_v, next_src, cur_k + 1))

print(min(d[N]))
