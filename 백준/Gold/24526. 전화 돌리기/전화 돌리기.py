import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split(" "))
graph = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    src, dst = map(int, input().split(" "))
    graph[src].append(dst)
cycle = set()
visit = set()
answer = 0
def dfs(node):
    if node in cycle:
        return False
    cycle.add(node)
    for next_node in graph[node]:
        if dfs(next_node):
            continue
        return False
    
    visit.add(node)
    cycle.remove(node)
    return True
for node in range(1, N + 1):
    if node not in visit:
        dfs(node)
print(N - len(cycle))