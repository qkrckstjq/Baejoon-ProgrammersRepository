from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        graph = defaultdict(dict)
        graph[k][k] = 0
        min_heap = []
        for src, dst, w in times:
            graph[src][dst] = w
            if src == k:
                heapq.heappush(min_heap, (w, dst))
        while min_heap:
            cur_w, cur_src = heapq.heappop(min_heap)
            for next_dst, w in graph[cur_src].items():
                next_w = w + cur_w
                if not next_dst in graph[k] or next_w < graph[k][next_dst]:
                    graph[k][next_dst] = next_w
                    heapq.heappush(min_heap, (next_w, next_dst))
        # print(graph)
        return -1 if len(list(graph[k].keys())) != n else max(list(graph[k].values()))
        
        