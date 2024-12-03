import heapq

N, M = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}
result = [['-' for _ in range(N)] for _ in range(N)]
for _ in range(M):
    src, dst, v = map(int, input().split(" "))
    graph[src].append((dst, v))
    graph[dst].append((src, v))

for i in range(1, N + 1):
    d = [float('inf') for _ in range(N + 1)]
    d[i] = 0
    queue = []
    for next_src, next_v in graph[i]:
        d[next_src] = next_v
        result[i - 1][next_src - 1] = str(next_src)
        heapq.heappush(queue, (next_v, next_src, next_src))
    while queue:
        cur_v, cur_src, cur_start = heapq.heappop(queue)
        if d[cur_src] < cur_v:
            continue
        for next_src, next_v in graph[cur_src]:
            total_v = cur_v + next_v
            if d[next_src] > total_v:
                d[next_src] = total_v
                result[i - 1][next_src - 1] = str(cur_start)
                heapq.heappush(queue, (total_v, next_src, cur_start))

[print(' '.join(a)) for a in result]
