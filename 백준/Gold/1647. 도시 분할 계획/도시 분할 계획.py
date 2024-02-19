import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

vertex, edge = list(map(int, s_input().split(" ")))

graph = defaultdict(dict)

for _ in range(edge):
    src, dst, w = list(map(int, s_input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

min_heap = []
result = 0
heapq.heappush(min_heap, (0, 1))
visit = set()
max_w = 0
while min_heap:
    cur_w, cur_node = heapq.heappop(min_heap)
    if cur_node in visit:
        continue
    result += cur_w
    max_w = max(cur_w, max_w)
    visit.add(cur_node)
    for next_node in list(graph[cur_node].keys()):
        if next_node not in visit:
            heapq.heappush(min_heap, (graph[cur_node][next_node], next_node))

print(result - max_w)