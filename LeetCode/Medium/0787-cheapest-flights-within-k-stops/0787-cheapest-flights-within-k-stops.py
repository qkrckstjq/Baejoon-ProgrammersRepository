import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        min_heap = []
        for u, v, w in flights:
            graph[u][v] = w
            if u == src:
                heapq.heappush(min_heap, (w, v, 0))
        visit = {}
        while min_heap:
            cur_w, cur_src, cur_k = heapq.heappop(min_heap)
            visit[cur_src] = cur_k
            if dst == cur_src:
                return cur_w
            if cur_k < k:
                for next_dst, w in graph[cur_src].items():
                    next_w = w + cur_w
                    if not next_dst in visit or cur_k + 1 < visit[next_dst]:
                        heapq.heappush(min_heap, (next_w, next_dst, cur_k + 1))
        return -1