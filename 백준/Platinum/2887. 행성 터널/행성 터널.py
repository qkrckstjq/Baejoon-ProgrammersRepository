import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

vertex_num = int(s_input())
vertex_info = []
min_x = []
min_y = []
min_z = []
for i in range(vertex_num):
    x, y, z = list(map(int, s_input().split(" ")))
    min_x.append((x, i))
    min_y.append((y, i))
    min_z.append((z, i))
min_x.sort(key=lambda a:a[0])
min_y.sort(key=lambda a:a[0])
min_z.sort(key=lambda a:a[0])

graph = defaultdict(dict)
for min_info in [min_x, min_y, min_z]:
    for i in range(len(min_info) - 1):
        if min_info[i + 1][1] in graph[min_info[i][1]]:
            past_w = graph[min_info[i][1]][min_info[i + 1][1]]
            graph[min_info[i][1]][min_info[i + 1][1]] = min(abs(min_info[i][0] - min_info[i + 1][0]), past_w)
        else:
            graph[min_info[i][1]][min_info[i + 1][1]] = abs(min_info[i][0] - min_info[i + 1][0])

        if min_info[i][1] in graph[min_info[i + 1][1]]:
            past_w = graph[min_info[i + 1][1]][min_info[i][1]]
            graph[min_info[i + 1][1]][min_info[i][1]] = min(abs(min_info[i + 1][0] - min_info[i][0]), past_w)
        else:
            graph[min_info[i + 1][1]][min_info[i][1]] = abs(min_info[i + 1][0] - min_info[i][0])
result = 0
connected_vertex = 0
min_heap = []
visit = set()
heapq.heappush(min_heap, (0, 0))
while min_heap:
    cur_w, cur_v = heapq.heappop(min_heap)
    if cur_v in visit:
        continue
    visit.add(cur_v)
    result += cur_w
    connected_vertex += 1
    if connected_vertex == vertex_num:
        break
    for next_v in list(graph[cur_v].keys()):
        if not next_v in visit:
            heapq.heappush(min_heap, (graph[cur_v][next_v], next_v))

print(result)