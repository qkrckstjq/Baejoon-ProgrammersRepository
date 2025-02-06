from collections import deque
N = int(input())
M = int(input())
graph = {i : {"need" : 0} for i in range(1, N + 1)}
indegree = [0 for _ in range(N + 1)]
for _ in range(M):
    dst, req, num = map(int, input().split(" "))
    graph[dst][req] = num
    indegree[req] += 1
    
# print(indegree)
queue = deque([N])
while queue:
    cur_node = queue.popleft()
    time = (1 if graph[cur_node]["need"] == 0 else graph[cur_node]["need"])
    
    for dst, num in graph[cur_node].items():
        if dst == "need":
            continue
        indegree[dst] -= 1
        if indegree[dst] <= 0:    
            queue.append(dst)
        graph[dst]["need"] += (num * time)
    # print(graph)

for i in range(1, N + 1):
    items = list(graph[i].keys())
    if len(items) == 1:
        print(f"{i} {graph[i]['need']}")
    else:
        continue
    
    