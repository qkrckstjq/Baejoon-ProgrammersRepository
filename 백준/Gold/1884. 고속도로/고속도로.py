import heapq
money = int(input())
N = int(input())
M = int(input())
graph = {i : [] for i in range(1, N + 1)}
d = [[float('inf') for _ in range(money + 1)] for _ in range(N + 1)]
for _ in range(M):
    src, dst, dis, cost = map(int, input().split(" "))
    graph[src].append((dst, dis, cost))

queue = []
heapq.heappush(queue, (0, 1, 0)) #거리, 노드, 사용한 비용

while queue:
    cur_dis, cur_src, cur_cost = heapq.heappop(queue)
    
    if cur_dis > d[cur_src][cur_cost]:
        continue
    
    for next_src, next_dis, next_cost in graph[cur_src]:
        total_dis = next_dis + cur_dis
        total_cost = cur_cost + next_cost
        if total_cost <= money and total_dis < d[next_src][total_cost]:
            d[next_src][total_cost] = total_dis
            heapq.heappush(queue, (total_dis, next_src, total_cost))

min_dis = min(d[N])

if min_dis == float('inf'):
    print(-1)
else:
    print(min_dis)
            