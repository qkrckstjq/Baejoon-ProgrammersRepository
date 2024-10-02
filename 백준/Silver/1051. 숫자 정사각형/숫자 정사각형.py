N, M = list(map(int, input().split(" ")))
graph = list()
for _ in range(N):
    row = list(map(int, input()))
    graph.append(row)
if N == 1 or M == 1:
    print(1)
else:
    answer = 1
    for i in range(N):
        for j in range(M):
            target = graph[i][j]
            k = 1
            while (i + k < len(graph)) and (j + k < len(graph[0])):
                if graph[i][j + k] == target and graph[i + k][j] == target and graph[i + k][j + k] == target:
                    answer = max((k + 1)**2, answer)
                k += 1
    print(answer)