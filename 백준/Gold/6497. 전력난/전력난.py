import heapq

while True:
    N, M = map(int, input().split(" "))
    if N == 0 and M == 0:
        break
    graph = {i : {} for i in range(0, N)}
    total_value = 0
    for _ in range(M):
        src, dst, val = map(int, input().split(" "))
        if dst in graph[src]:
            graph[src][dst] = min(val, graph[src][dst])
        else:
            graph[src][dst] = val
        
        if src in graph[dst]:
            graph[dst][src] = min(val, graph[dst][src])
        else:
            graph[dst][src] = val
        total_value += val
    queue = []
    heapq.heappush(queue, (0, 0))
    visit = set()
    cnt = 0
    answer = 0

    while queue:
        cur_value, cur_vertex = heapq.heappop(queue)
        if cur_vertex in visit:
            continue    
        visit.add(cur_vertex)
        cnt += 1
        answer += cur_value
        if cnt == N:
            break
        
        for dst, value in graph[cur_vertex].items():
            if dst not in visit:
                heapq.heappush(queue, (value, dst))

    print(total_value - answer)    
