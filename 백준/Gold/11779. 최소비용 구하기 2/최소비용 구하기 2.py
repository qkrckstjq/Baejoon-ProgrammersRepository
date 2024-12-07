import heapq

N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N + 1)}

# 그래프 입력
for _ in range(M):
    src, dst, v = map(int, input().split())
    graph[src].append((dst, v))

start, end = map(int, input().split())

# 거리 초기화
d = [float('inf')] * (N + 1)
d[start] = 0

# 이전 노드를 기록 (경로 추적용)
prev = [None] * (N + 1)

# 다익스트라를 위한 우선순위 큐
queue = []
heapq.heappush(queue, (0, start))

while queue:
    cur_dist, cur_node = heapq.heappop(queue)

    # 이미 처리된 노드면 건너뜀
    if d[cur_node] < cur_dist:
        continue

    # 인접 노드 탐색
    for next_node, weight in graph[cur_node]:
        total_dist = cur_dist + weight
        if d[next_node] > total_dist:
            d[next_node] = total_dist
            prev[next_node] = cur_node  # 이전 노드 기록
            heapq.heappush(queue, (total_dist, next_node))

# 최단 거리 출력
print(d[end])

# 최단 경로 추적
path = []
current = end
while current:
    path.append(current)
    current = prev[current]
path.reverse()

# 최단 경로 출력
print(len(path))
print(" ".join(map(str, path)))
