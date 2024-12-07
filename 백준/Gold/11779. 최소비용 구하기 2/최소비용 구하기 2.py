import heapq
N = int(input())
M = int(input())
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    src, dst, v = map(int, input().split(" "))
    graph[src].append((dst, v))
start, end = map(int, input().split(" "))
# print(graph, start, end)
d = [float('inf') for _ in range(N + 1)]
d[start] = 0

queue = []
heapq.heappush(queue, (0, start, f"{start}"))

route = ""
while queue:
    cur_v, cur_src, cur_route = heapq.heappop(queue)
    if d[cur_src] < cur_v:
        continue
    for next_src, next_v in graph[cur_src]:
        total_v = next_v + cur_v
        if d[next_src] > total_v:
            d[next_src] = total_v
            next_route = f"{cur_route} {next_src}"
            heapq.heappush(queue, (total_v, next_src, next_route))
            if next_src == end:
                route = next_route

print(d[end])
print(len(route.split(" ")))
print(route)