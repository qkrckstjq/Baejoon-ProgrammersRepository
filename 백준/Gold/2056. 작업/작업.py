from collections import deque

N = int(input())
graph = {i: [] for i in range(1, N + 1)}
delay = [0 for _ in range(N + 1)]
dp = {}

for i in range(1, N + 1):
    input_list = list(map(int, input().split()))
    delay[i] = input_list[0]
    for j in range(2, 2 + input_list[1]):
        graph[i].append(input_list[j])
        
start = [node for node in range(1, N + 1) if len(graph[node]) == 0]

result = []
def dfs(node):
    if node in dp:
        return dp[node] 
    global delay, result, graph
    childrens = [0]
    if node in graph:
        for require_node in graph[node]:
            childrens.append(dfs(require_node))
    longest_child = max(childrens)
    dp[node] = delay[node] + longest_child
    return dp[node]
    
for node in range(1, N + 1):
    result.append(dfs(node))

print(max(result))