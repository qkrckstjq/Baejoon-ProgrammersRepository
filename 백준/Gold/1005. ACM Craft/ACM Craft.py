T = int(input())

def dfs(target, graph, delay, memo):
    if target in memo:
        return memo[target]
    childrens = [0]
    if target in graph:
        for require in graph[target]:
            childrens.append(dfs(require, graph, delay, memo))
    longest_child = max(childrens)
    memo[target] = delay[target - 1] + longest_child
    return delay[target - 1] + longest_child
    
    
for _ in range(T):
    N, K = list(map(int, input().split(" ")))
    delay = list(map(int, input().split(" ")))
    graph = {}
    for _ in range(K):
        require, dst = list(map(int, input().split(" "))) #dst를 짓기 위해서 require가 필요함
        if dst in graph:
            graph[dst].append(require)
        else:
            graph[dst] = [require]
    target = int(input())
    memo = {}
    print(dfs(target, graph, delay, memo))