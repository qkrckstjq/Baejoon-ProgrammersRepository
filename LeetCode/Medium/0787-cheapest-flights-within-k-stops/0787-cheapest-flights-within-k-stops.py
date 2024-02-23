import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        max_d = 987654321
        graph = [[] for _ in range(n + 1)]
        dijkstra = [max_d] * (n + 1)
        dijkstra[src] = 0
        min_heap = []
        visit = {}
        for edge in flights:
            u, v, w = edge
            graph[u].append((v, w))
            if u == src:
                dijkstra[v] = w
                heapq.heappush(min_heap, (w, v, 0))
                
        while min_heap:
            cur_w, cur_dst, cur_k = heapq.heappop(min_heap)
            if cur_dst == dst:
                return cur_w
            if cur_dst not in visit or cur_k < visit[cur_dst]:
                visit[cur_dst] = cur_k
                if cur_k < k:
                    for next_dst, w in graph[cur_dst]:
                        next_w = w + cur_w
                        dijkstra[next_dst] = next_w
                        heapq.heappush(min_heap, (next_w, next_dst, cur_k + 1))
        return - 1