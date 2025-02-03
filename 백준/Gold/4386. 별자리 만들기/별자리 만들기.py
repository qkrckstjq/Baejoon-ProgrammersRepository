import heapq
N = int(input())

arr = []
for i in range(N):
    x, y = list(map(float, input().split(" ")))
    arr.append((y, x, i))

graph = {i : {} for i in range(N)}

def dist(y, x, y1, x1):
    return ((y - y1)**2 + (x - x1)**2)**0.5

for a in arr:
    for b in arr:
        if a[2] == b[2]:
            continue
        graph[a[2]][b[2]] = dist(a[0], a[1], b[0], b[1])

queue = []
vertex_num = 0
visit = set()
answer = 0
heapq.heappush(queue, (0, 0))
while queue:
    cur_value, cur_vertex = heapq.heappop(queue)
    if cur_vertex in visit:
        continue
    visit.add(cur_vertex)
    if vertex_num == N:
        break
    vertex_num += 1
    answer += cur_value
    
    for next_vertex, next_value in graph[cur_vertex].items():
        if next_vertex in visit:
            continue
        heapq.heappush(queue, (next_value, next_vertex))
    
print(round(answer, 2))