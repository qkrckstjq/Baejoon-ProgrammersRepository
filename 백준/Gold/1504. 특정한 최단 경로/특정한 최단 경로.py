import heapq

N, E = list(map(int, input().split(" ")))
graph = {i: {} for i in range(1, N+1)}  # 모든 노드를 초기화        

for _ in range(E):
    src, dst, w = list(map(int, input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w  # 양방향 그래프

target1, target2 = list(map(int, input().split(" ")))

def dieck(src, dst):
    min_heap = [(0, src)]
    visit = set()
    dist = {src: 0}
    
    while min_heap:
        cur_w, cur_src = heapq.heappop(min_heap)
        if cur_src in visit:
            continue
        visit.add(cur_src)
        
        if cur_src == dst:
            return cur_w
        
        for next_dst, w in graph[cur_src].items():
            next_w = cur_w + w
            if dist.get(next_dst, float('inf')) > next_w:
                dist[next_dst] = next_w
                heapq.heappush(min_heap, (next_w, next_dst))

    return float('inf')

case1 = dieck(1, target1) + dieck(target1, target2) + dieck(target2, N)
case2 = dieck(1, target2) + dieck(target2, target1) + dieck(target1, N)

if case1 == float('inf') and case2 == float('inf'):
    print(-1)
else:
    print(min(case1, case2))
