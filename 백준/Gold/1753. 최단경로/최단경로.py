import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

v, e = list(map(int, s_input().split(" ")))
start = int(s_input())
min_heap = []
graph = defaultdict(list)
# graph[start].append((start, 0))
for i in range(e):
    src, dst, w = list(map(int, s_input().split(" ")))
    graph[src].append((w, dst))
    if src == start:
        heapq.heappush(min_heap, (w, dst))

result = [987654321] * (v + 1)
heapq.heappush(min_heap, (0, start))
while min_heap:
    cur_w, cur_dst = heapq.heappop(min_heap)
    if result[cur_dst] < cur_w:
        continue
    for next_w, next_dst in graph[cur_dst]:
        if cur_w + next_w < result[next_dst]:
            result[next_dst] = cur_w + next_w
            heapq.heappush(min_heap, (cur_w + next_w, next_dst))

result[start] = 0
for i in range(1, len(result)):
    if result[i] == 987654321:
        print("INF")
    else:
        print(result[i])