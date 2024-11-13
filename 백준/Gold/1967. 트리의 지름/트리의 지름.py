import heapq, sys
sys.setrecursionlimit(100000)
n = int(input())
graph = {}
for _ in range(n - 1):
    s, d, w = list(map(int, input().split(" ")))
    if s in graph:
        graph[s][d] = w
    else:
        graph[s] = {d : w}
    # if d in graph:
    #     graph[d][s] = w
    # else:
    #     graph[d] = {s : w}
#[가장 긴 자식, 현재 위치에서 가장 긴 지름]
def dfs(node, tree, weight):
    global result
    childrens = []
    if node in tree:
        for next_node, w in tree[node].items():
            childrens.append(dfs(next_node, tree, w))
    if len(childrens) == 0:
        return weight
    elif len(childrens) == 1:
        result = max(result, weight + childrens[0])
        return weight + childrens[0]
    else:
        childrens.sort(reverse=True)
        result = max(result, childrens[0] + childrens[1])
        return weight + childrens[0]
    

result = 0
dfs(1, graph, 0)
print(result)
    