import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    pq = [(0, 1)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue

        for next_node, cost in graph[current_node]:
            new_dist = current_dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return sum(1 for dist in distance[1:] if dist <= K)