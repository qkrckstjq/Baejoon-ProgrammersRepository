from typing import List
import heapq

INF = float('inf')

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        pq = [(0, src, 0)]
        
        dist = [[INF for _ in range(k+2)] for _ in range(n)]
        dist[src][0] = 0
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
       
            if stops > k:
                continue
            
            for next_node, w in graph[node]:
                next_cost = cost + w

                if next_cost < dist[next_node][stops + 1]:
                    dist[next_node][stops + 1] = next_cost
                    heapq.heappush(pq, (next_cost, next_node, stops + 1))

        return -1