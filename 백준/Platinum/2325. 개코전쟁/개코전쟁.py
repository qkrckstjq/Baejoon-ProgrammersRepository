import heapq

N, M = map(int, input().split(" "))
graph = {i : {} for i in range(1, N + 1)}
d = [float('inf') for _ in range(N + 1)]
for _ in range(M):
    src, dst, v = map(int, input().split(" "))
    graph[src][dst] = v
    graph[dst][src] = v

def dijk():
    d = [float('inf') for _ in range(N + 1)]
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cur_v, cur_src = heapq.heappop(queue)
        if d[cur_src] < cur_v:
            continue
        for next_src, next_v in graph[cur_src].items():
            total_v = next_v + cur_v
            if d[next_src] > total_v:
                d[next_src] = total_v
                heapq.heappush(queue, (total_v, next_src))
    return d[N]

queue = []
min_route = ""
heapq.heappush(queue, (0, 1, "1"))
while queue:
    cur_v, cur_src, cur_route = heapq.heappop(queue)
    if d[cur_src] < cur_v:
        continue
    for next_src, next_v in graph[cur_src].items():
        total_v = next_v + cur_v
        if d[next_src] > total_v:
            d[next_src] = total_v
            next_route = f"{cur_route} {next_src}"
            heapq.heappush(queue, (total_v, next_src, next_route))
            if next_src == N:
                min_route = next_route
result = d[N]
min_route = list(map(int, min_route.split(" ")))

for i in range(len(min_route) - 1):
    src = min_route[i]
    dst = min_route[i + 1]                
    temp_v = graph[src][dst]
    del graph[src][dst]
    del graph[dst][src]

    result = max(result, dijk())
    graph[src][dst] = temp_v
    graph[dst][src] = temp_v

print(result)