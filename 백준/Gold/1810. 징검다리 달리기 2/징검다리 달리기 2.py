import heapq

N, F = map(int, input().split(" "))
coord = set([(0, 0)])
graph = {}
d = {}

def get_dis(y1, x1, y2, x2):
    return ((y1 - y2)**2 + (x1 - x2)**2)**0.5

def check_move(y1, x1, y2, x2):
    return True if abs(y1 - y2) <= 2 and abs(x1 - x2) <= 2 else False

for _ in range(N):
    y, x = map(int, input().split(" "))
    coord.add((y, x))
    d[(y, x)] = float('inf')
d[(0, 0)] = 0
# for i in range(len(coord)):
#     y, x = coord[i][0], coord[i][1]
#     for j in range(len(coord)):
#         if i != j:
#             n_y, n_x = coord[j][0], coord[j][1]
#             if check_move(y, x, n_y, n_x):
#                 if (y, x) in graph:
#                     graph[(y, x)].append((n_y, n_x))
#                 else:
#                     graph[(y, x)] = [(n_y, n_x)]

queue = []
heapq.heappush(queue, (0, 0, 0))
result = float('inf')
while queue:
    cur_dist, cur_y, cur_x = heapq.heappop(queue)
    if d[(cur_y, cur_x)] < cur_dist:
        continue
    for i in range(-2, 3, 1):
        for j in range(-2, 3, 1):
            next_y, next_x = cur_y + i, cur_x + j
            if ((next_y != cur_y) or (next_x != cur_x)) and (next_y, next_x) in coord:
                next_dist = cur_dist + get_dis(cur_y, cur_x, next_y, next_x)
                if d[(next_y, next_x)] > next_dist:
                    d[(next_y, next_x)] = next_dist
                    heapq.heappush(queue, (next_dist, next_y, next_x))
                    if next_x == F:
                        result = min(result, next_dist)             
                        
if result == float('inf'):
    print(-1)
else:
    print(int(round(result, 0)))