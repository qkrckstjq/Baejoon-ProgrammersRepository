import heapq

N, E = map(int, input().split(" "))
graph = {i: {} for i in range(1, N+1)}  # 모든 노드 초기화        

for _ in range(E):
    src, dst, w = map(int, input().split(" "))
    graph[src][dst] = w
    graph[dst][src] = w

target1, target2 = map(int, input().split(" "))

def dijkstra(src, dst):
    min_heap = [(0, src)]
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[src] = 0
    visit = set()
    
    while min_heap:
        cur_w, cur_src = heapq.heappop(min_heap)
        if cur_src in visit:
            continue
        visit.add(cur_src)
        
        if cur_src == dst:
            return cur_w
        
        for next_dst, next_w in graph[cur_src].items():
            if next_dst not in visit:
                new_w = cur_w + next_w
                if new_w < distances[next_dst]:
                    distances[next_dst] = new_w
                    heapq.heappush(min_heap, (new_w, next_dst))
    
    return float('inf')  # 경로가 없을 경우 무한대 반환

# 가능한 경로 계산
case1 = dijkstra(1, target1) + dijkstra(target1, target2) + dijkstra(target2, N)
case2 = dijkstra(1, target2) + dijkstra(target2, target1) + dijkstra(target1, N)

# 결과 확인
result = min(case1, case2)

if result == float('inf'):
    print(-1)
else:
    print(result)
