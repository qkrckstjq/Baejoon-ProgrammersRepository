N, M = list(map(int, input().split(" ")))
graph = {i : [] for i in range(1, N + 1)}
know = list(map(int, input().split(" ")))
parties = []
for i in range(1, len(know) - 1):
    # if i + 1 < len(know):
    graph[know[i]].append(know[i + 1])
    graph[know[i + 1]].append(know[i])

for _ in range(M):
    vertexes = list(map(int, input().split(" ")))
    parties.append(vertexes[1:])
    for i in range(1, len(vertexes) - 1):
    # if i + 1 < len(know):
        graph[vertexes[i]].append(vertexes[i + 1])
        graph[vertexes[i + 1]].append(vertexes[i])

visit = set()
stack = []
if len(know) > 1:
    stack.append(know[1])
    visit.add(know[1])

while stack:
    cur_v = stack.pop()
    for next_v in graph[cur_v]:
        if next_v not in visit:
            visit.add(next_v)
            stack.append(next_v)

result = 0
for i in range(len(parties)):
    is_possible = True
    party = parties[i]
    for v in party:
        if v in visit:
            is_possible = False
            break
    if is_possible:
        result += 1
    
print(result)