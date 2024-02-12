import heapq, sys
from collections import defaultdict

def sInput():
    return sys.stdin.readline().strip()

v_e = sInput().split(" ")

vertex = int(v_e[0])
edge = int(v_e[1])
graph = defaultdict(dict)
min_heap = []
visit = set()
for i in range(edge):
    src, dst, w = list(map(int, sInput().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

result = 0
heapq.heappush(min_heap, (0, 1)) #튜플형식 (가중치, 정점) 힙에서는 첫번째 인자를 기준으로 비교를 한단다

while min_heap:
    cur_min = heapq.heappop(min_heap)
    cur_vertex = cur_min[1]
    if cur_vertex in visit:
        continue

    result += cur_min[0]
    visit.add(cur_vertex)
    for dst in graph[cur_vertex]:
        if dst not in visit:
            heapq.heappush(min_heap, (graph[cur_vertex][dst], dst))


print(result)








