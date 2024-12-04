# import heapq
# def dijk(N, start, end, graph):
#     d = [float('inf') for _ in range(N)]
#     d[start] = 0
#     queue = []
#     heapq.heappush(queue, (0, start))
#     while queue:
#         cur_v, cur_src = heapq.heappop(queue)
#         if d[cur_src] < cur_v:
#             continue
#         for next_src, next_v in graph[cur_src].items():
#             total_v = cur_v + next_v
#             if d[next_src] > total_v:
#                 d[next_src] = total_v
#                 heapq.heappush(queue, (total_v, next_src))
#     return d[end]

# result = []    

# while True:
#     N, M = map(int, input().split(" "))
#     if N == 0 and M == 0:
#         break
#     start, end = map(int, input().split(" "))
#     graph = {i : {} for i in range(N)}
    
#     for _ in range(M):
#         src, dst, v = map(int, input().split(" "))
#         graph[src][dst] = v
    
#     d = [float('inf') for _ in range(N)]
#     d[start] = 0
#     queue = []
    
#     min_route = []
    
#     heapq.heappush(queue, (0, start, f"{start}"))
#     while queue:
#         cur_v, cur_src, cur_route = heapq.heappop(queue)
#         if d[cur_src] < cur_v:
#             continue
#         for next_src, next_v in graph[cur_src].items():
#             total_v = cur_v + next_v
#             next_route = f"{cur_route} {next_src}"
#             if d[next_src] > total_v:
#                 d[next_src] = total_v
#                 heapq.heappush(queue, (total_v, next_src, next_route))
#                 if next_src == end:
#                     min_route = [list(map(int, next_route.split(" ")))]
#             elif d[next_src] == total_v and next_src == end:
#                 min_route.append(list(map(int, next_route.split(" "))))
#             elif d[next_src] == total_v:
#                 heapq.heappush(queue, (total_v, next_src, next_route))
    
#     # print(min_route)
#     # print(graph)
    
#     for route in min_route:
#         for i in range(len(route) - 1):
#             src = route[i]
#             dst = route[i + 1]
#             if src in graph and dst in graph[src]:
#                 del graph[src][dst]
    
#     # print(graph)

#     result.append(dijk(N, start, end, graph))
    
# [print(num if num != float('inf') else -1) for num in result]
import heapq
from collections import defaultdict, deque

def dijkstra(N, start, graph, removed):
    d = [float('inf')] * N
    d[start] = 0
    queue = [(0, start)]
    parent = defaultdict(list)  # 부모 노드 저장 (최단 경로 추적용)

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if d[cur_node] < cur_dist:
            continue

        for next_node, weight in graph[cur_node]:
            if (cur_node, next_node) in removed:  # 제거된 간선은 무시
                continue

            total_dist = cur_dist + weight
            if total_dist < d[next_node]:
                d[next_node] = total_dist
                heapq.heappush(queue, (total_dist, next_node))
                parent[next_node] = [cur_node]
            elif total_dist == d[next_node]:
                parent[next_node].append(cur_node)

    return d, parent


def remove_shortest_paths(end, parent, removed):
    # BFS로 역추적하며 간선 제거
    queue = deque([end])
    while queue:
        node = queue.popleft()
        for prev in parent[node]:
            if (prev, node) not in removed:
                removed.add((prev, node))  # 간선 비활성화
                queue.append(prev)


result = []

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    start, end = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))

    # Step 1: 최단 경로 계산
    d, parent = dijkstra(N, start, graph, set())

    # Step 2: 최단 경로 간선 제거
    removed = set()  # 제거된 간선을 기록
    remove_shortest_paths(end, parent, removed)

    # Step 3: 거의 최단 경로 계산
    d_after_removal, _ = dijkstra(N, start, graph, removed)
    result.append(d_after_removal[end] if d_after_removal[end] != float('inf') else -1)

# 결과 출력
for res in result:
    print(res)
