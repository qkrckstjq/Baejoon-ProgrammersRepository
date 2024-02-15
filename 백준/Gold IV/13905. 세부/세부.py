import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

vertex, edge = list(map(int, s_input().split(" ")))
start, end = list(map(int, s_input().split(" ")))

graph = defaultdict(dict)
visit = set()
for _ in range(edge):
    src, dst, w = list(map(int, s_input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

min_heap = []
result = 1000000
heapq.heappush(min_heap, (-result, start))
mst_tree = defaultdict(dict)

while min_heap:
    cur_w, cur_node = heapq.heappop(min_heap)
    cur_w = cur_w * -1
    if cur_node in visit:
        continue
    result = min(cur_w, result)
    if cur_node == end:
        print(result)
        break
    visit.add(cur_node)
    for next_node in list(graph[cur_node].keys()):
        heapq.heappush(min_heap, (-graph[cur_node][next_node], next_node))
    if not min_heap:
        print(0)

