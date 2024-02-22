from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for edge in times:
            src, dst, w = edge
            graph[src][dst] = w
            
        min_heap = []
        for dst in list(graph[k].keys()):
            heapq.heappush(min_heap, (graph[k][dst], dst))
        
        visit = set()
        while min_heap:
            cur_w, cur_dst = heapq.heappop(min_heap)
            visit.add(cur_dst)
            for dst in list(graph[cur_dst].keys()):
                if (not dst in graph[k] or graph[k][cur_dst] + graph[cur_dst][dst] < graph[k][dst]) and dst != k:
                    graph[k][dst] = graph[k][cur_dst] + graph[cur_dst][dst]
                    heapq.heappush(min_heap, (graph[k][dst], dst))
        return max(list(graph[k].values())) if len(visit) + 1 == n else -1