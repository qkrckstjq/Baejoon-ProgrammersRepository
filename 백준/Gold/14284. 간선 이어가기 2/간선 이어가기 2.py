import heapq

v, e = list(map(int, input().split(" ")))
graph = {i : {} for i in range(1, v + 1)}

for _ in range(e):
    src, dst, w = list(map(int, input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

start, end = list(map(int, input().split(" ")))
d = [float('inf') for _ in range(v + 1)]
d[start] = 0
min_heap = []
heapq.heappush(min_heap, (0, start))
while min_heap:
    cur_v, cur_src = heapq.heappop(min_heap)
    if d[cur_src] < cur_v:
        continue
    for next_src, next_v in graph[cur_src].items():
        total_v = next_v + cur_v
        if total_v < d[next_src]:
            d[next_src] = total_v
            heapq.heappush(min_heap, (total_v, next_src))

print(d[end])


    