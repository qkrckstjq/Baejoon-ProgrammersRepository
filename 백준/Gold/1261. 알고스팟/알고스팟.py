import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

max_d = 987654321
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def is_possible(N, M, y, x):
    return True if 0 <= y < M and 0 <= x < N else False

result = []
N, M = list(map(int, s_input().split(" ")))
graph = []
dijkstra = []
min_heap = []
for i in range(M):
    x = list(s_input())
    temp = [max_d] * len(x)
    dijkstra.append(temp)
    graph.append(x)
heapq.heappush(min_heap, (0, 0, 0))
dijkstra[0][0] = 0
while min_heap:
    cur_w, cur_y, cur_x = heapq.heappop(min_heap)
    if cur_y == M - 1 and cur_x == N - 1:
        print(cur_w)
        break
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if not is_possible(N, M, next_y, next_x):
            continue

        next_w = cur_w + int(graph[next_y][next_x])
        if next_w < dijkstra[next_y][next_x]:
            dijkstra[next_y][next_x] = next_w
            heapq.heappush(min_heap, (next_w, next_y, next_x))