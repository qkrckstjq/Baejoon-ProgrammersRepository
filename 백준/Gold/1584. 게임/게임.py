import sys, heapq
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

max_d = 987654321
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def is_possible(y, x):
    return True if 0 <= y <= 500 and 0 <= x <= 500 else False

def check_zone(arr, y, x):
    for x1, y1, x2, y2 in arr:
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True
    return False


danger_zone = []
dead_zone = []
N = int(s_input())
for _ in range(N):
    x1, y1, x2, y2 = list(map(int, s_input().split(" ")))
    danger_zone.append((x1, y1, x2, y2))

M = int(s_input())
for _ in range(M):
    x1, y1, x2, y2 = list(map(int, s_input().split(" ")))
    dead_zone.append((x1, y1, x2, y2))

dijkstra = [[max_d] * 501 for _ in range(501)]
min_heap = []
heapq.heappush(min_heap, (0, 0, 0))
dijkstra[0][0] = 0
while min_heap:
    cur_w, cur_y, cur_x = heapq.heappop(min_heap)
    if cur_y == 500 and cur_x == 500:
        print(cur_w)
        break
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        next_w = cur_w
        if not is_possible(next_y, next_x) or check_zone(dead_zone, next_y, next_x):
            continue

        if check_zone(danger_zone, next_y, next_x):
            next_w += 1

        if next_w < dijkstra[next_y][next_x]:
            dijkstra[next_y][next_x] = next_w
            heapq.heappush(min_heap, (next_w, next_y, next_x))
else:
    print(-1)