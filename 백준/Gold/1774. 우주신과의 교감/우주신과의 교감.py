import heapq, math
N, M = map(int, input().split(" "))
grid = []
graph = {i : {} for i in range(1, N + 1)}
for i in range(N):
    y, x = map(int, input().split(" "))
    grid.append((y, x, i + 1))

for y, x, i in grid:
    for y1, x1, j in grid:
        if i == j:
            continue
        dst = math.sqrt((y - y1) ** 2 + (x - x1) ** 2)
        graph[i][j] = dst
        graph[j][i] = dst

for _ in range(M):
    y, x = map(int, input().split(" "))
    graph[y][x] = 0
    graph[x][y] = 0

queue = []
visit = set()
heapq.heappush(queue, (0, 1))
vertex_count = 0
answer = 0
while queue:
    cur_value, cur_vertex = heapq.heappop(queue)
    if cur_vertex in visit:
        continue
    visit.add(cur_vertex)
    answer += cur_value
    vertex_count += 1
    if vertex_count == N:
        break
    for dst, value in graph[cur_vertex].items():
        if dst not in visit:
            heapq.heappush(queue, (value, dst))

print(format(answer, ".2f"))