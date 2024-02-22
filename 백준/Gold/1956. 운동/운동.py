import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().strip().split())
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().strip().split())
    graph[a][b] = c

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = INF
# 사이클을 형성(출발점과 도착점이 같아야함)
for i in range(1, V+1):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)