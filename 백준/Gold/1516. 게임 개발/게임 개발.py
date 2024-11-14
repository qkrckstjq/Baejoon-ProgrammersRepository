N = int(input())
graph = {}
delay = []
memo = {}
def dfs(node, graph, delay):
    if node in memo:
        return memo[node]
    childrens = [0]
    if node in graph:
        for require in graph[node]:
            childrens.append(dfs(require, graph, delay))
    longest_child = max(childrens)
    memo[node] = longest_child + delay[node - 1]
    return longest_child + delay[node - 1]
    
for i in range(N):
    a = list(map(int, input().split(" ")))
    delay.append(a[0])
    graph[i + 1] = []
    for j in range(1, len(a) - 1):
        graph[i + 1].append(a[j])

for i in range(1, N + 1):
    dfs(i, graph, delay)

for i in range(1, N + 1):
    print(memo[i])