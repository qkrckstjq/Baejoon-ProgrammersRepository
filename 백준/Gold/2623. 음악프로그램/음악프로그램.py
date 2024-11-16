N, M = list(map(int, input().split(" ")))
graph = {i : [] for i in range(1, N + 1)}
indegree = [0 for i in range(N + 1)]

for _ in range(M):
    num, *order = list(map(int, input().split(" ")))
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            graph[order[i]].append(order[j])
            indegree[order[j]] += 1

stack = []
for num in range(1, len(indegree)):
    if indegree[num] == 0:
        stack.append(num)

result = []
while stack:
    cur_node = stack.pop()
    result.append(cur_node)
    for next_node in graph[cur_node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            stack.append(next_node)
if len(result) == N:
    for node in result:
        print(node)
else:
    print(0)
