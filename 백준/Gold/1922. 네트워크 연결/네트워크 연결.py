import sys, heapq
from collections import defaultdict


def s_input():
    return sys.stdin.readline().strip()


vertex = int(s_input())
edge = int(s_input())
graph = defaultdict(dict)
min_heap = []
visit = set()
for _ in range(edge):
    src, dst, w = list(map(int, s_input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

result = 0
heapq.heappush(min_heap, (0, 1))
connected_vertex = 0

while min_heap:
    cur_w, cur_node = heapq.heappop(min_heap)
    if cur_node in visit:
        continue
    visit.add(cur_node)
    connected_vertex += 1
    result += cur_w
    if connected_vertex == vertex:
        break
    for next_node in list(graph[cur_node].keys()):
        heapq.heappush(min_heap, (graph[cur_node][next_node], next_node))

print(result)