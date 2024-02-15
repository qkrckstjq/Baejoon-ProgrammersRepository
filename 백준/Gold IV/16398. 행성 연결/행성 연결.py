import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

vertex = int(s_input())

graph = defaultdict(dict)

index_y = 1
for _ in range(vertex):
    edge = list(map(int, s_input().split(" ")))
    for index_x in range(0, len(edge), 1):
        if edge[index_x] != 0:
            graph[index_y][index_x + 1] = edge[index_x]
    index_y += 1

result = 0
min_heap = []
visit = set()
heapq.heappush(min_heap, (0, 1))

while min_heap:
    cur_w, cur_node = heapq.heappop(min_heap)
    if cur_node in visit:
        continue
    visit.add(cur_node)
    result += cur_w
    for next in list(graph[cur_node].keys()):
        if not next in visit:
            heapq.heappush(min_heap, (graph[cur_node][next], next))

print(result)