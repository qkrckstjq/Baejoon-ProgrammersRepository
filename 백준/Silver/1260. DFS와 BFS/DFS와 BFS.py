import sys
from collections import deque

def dfs(graph, visit, start):
    stack = [start]
    result = []
    while stack:
        cur = stack.pop()
        if not visit[cur]:
            result.append(str(cur))
            visit[cur] = True
            if cur in graph:
                stack.extend(sorted(filter(lambda x: not visit[x], graph[cur]), reverse=True))
    return result

def bfs(graph, visit, start):
    queue = deque([start])
    result = []
    while queue:
        cur = queue.popleft()
        if not visit[cur]:
            result.append(str(cur))
            visit[cur] = True
            if cur in graph:
                queue.extend(sorted(filter(lambda x: not visit[x], graph[cur])))
    return result

def sInput():
    return sys.stdin.readline().strip()

N, M, V = map(int, sInput().split())

graph = {}
visit = {i: False for i in range(1, N + 1)}

for _ in range(M):
    src, dst = map(int, sInput().split())
    graph.setdefault(src, []).append(dst)
    graph.setdefault(dst, []).append(src)

for edge in graph:
    graph[edge] = sorted(graph[edge])

print(' '.join(dfs(graph, visit.copy(), V)))
print(' '.join(bfs(graph, visit.copy(), V)))