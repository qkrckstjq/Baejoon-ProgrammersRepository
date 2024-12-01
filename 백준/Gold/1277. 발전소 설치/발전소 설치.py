import heapq
import math

# 입력 처리
N, W = map(int, input().split())
M = float(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

# 인접 리스트 생성
graph = {i: [] for i in range(N)}

# 거리 계산 함수
def get_len(i, j):
    x1, y1 = lines[i]
    x2, y2 = lines[j]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# W개의 주어진 간선을 0 비용으로 추가
for _ in range(W):
    n1, n2 = map(int, input().split())
    n1, n2 = n1 - 1, n2 - 1
    graph[n1].append((n2, 0))
    graph[n2].append((n1, 0))

# 모든 노드 쌍에 대해 M 이하의 거리만 연결
for i in range(N):
    for j in range(i + 1, N):
        dist = get_len(i, j)
        if dist <= M:
            graph[i].append((j, dist))
            graph[j].append((i, dist))

# 다익스트라 알고리즘
dist = [float('inf')] * N
dist[0] = 0
pq = [(0, 0)]  # (거리, 노드)

while pq:
    cur_len, cur_node = heapq.heappop(pq)
    if dist[cur_node] < cur_len:
        continue

    for next_node, weight in graph[cur_node]:
        new_len = cur_len + weight
        if new_len < dist[next_node]:
            dist[next_node] = new_len
            heapq.heappush(pq, (new_len, next_node))

# 결과 출력
result = int(dist[N - 1] * 1000)
print(result)
            

