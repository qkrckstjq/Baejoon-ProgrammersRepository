T = int(input())

def dfs(node, graph):
    stack = [node]
    visit = set()
    answer = 0
    while stack:
        cur_node = stack.pop()
        if cur_node in visit:
            continue
        visit.add(cur_node)
        answer += 1
        for dst in graph[cur_node]:
            if dst not in visit:
                stack.append(dst)
    return answer - 1
    
for _ in range(T):
    N, M = map(int, input().split(" "))
    graph = {i : [] for i in range(1, N + 1)}
    for _ in range(M):
        src, dst = map(int, input().split(" "))
        graph[src].append(dst)
        graph[dst].append(src)
    print(dfs(1, graph))