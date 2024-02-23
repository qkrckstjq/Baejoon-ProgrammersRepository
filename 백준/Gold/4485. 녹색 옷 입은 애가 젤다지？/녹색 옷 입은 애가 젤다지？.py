import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

max_d = 987654321
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def is_possible(N, y, x):
    return True if 0 <= y < N and 0 <= x < N else False

result = []
while True:
    N = int(s_input())
    if N == 0:
        break
    graph = []
    dijkstra = []
    min_heap = []
    for i in range(N):
        x = list(map(int, s_input().split(" ")))
        temp = [max_d] * len(x)
        dijkstra.append(temp)
        graph.append(x)
    heapq.heappush(min_heap, (graph[0][0], 0, 0))
    dijkstra[0][0] = graph[0][0]
    while min_heap:
        cur_w, cur_y, cur_x = heapq.heappop(min_heap)
        if cur_y == N - 1 and cur_x == N - 1:
            result.append(cur_w)
            break
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if not is_possible(N, next_y, next_x):
                continue
            next_w = cur_w + graph[next_y][next_x]
            if next_w < dijkstra[next_y][next_x]:
                dijkstra[next_y][next_x] = next_w
                heapq.heappush(min_heap, (next_w, next_y, next_x))

for i in range(len(result)):
    print(f'Problem {i + 1}: {result[i]}')