import heapq
N, M, K = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}
d = [[] for _ in range(N + 1)]

for _ in range(M):
    src, dst, v = map(int, input().split(" "))
    graph[src].append((dst, v))

queue = []
heapq.heappush(d[1], 0)
heapq.heappush(queue, (0, 1))

while queue:
    cur_v, cur_src = heapq.heappop(queue)
    for next_src, next_v in graph[cur_src]:
        total_v = cur_v + next_v
        if len(d[next_src]) < K:
            heapq.heappush(d[next_src], -total_v)
            heapq.heappush(queue, (total_v, next_src))
        elif -total_v > d[next_src][0]:
            heapq.heappop(d[next_src])
            heapq.heappush(d[next_src], -total_v)
            heapq.heappush(queue, (total_v, next_src))

# print(d)

for i in range(1, N+1):
    if len(d[i]) == K:
        print(-d[i][0])
    else:
        print(-1)