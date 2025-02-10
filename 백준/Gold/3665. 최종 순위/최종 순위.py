T = int(input())

for _ in range(T):
    n = int(input())
    prev_ranks = list(map(int, input().split(" ")))
    m = int(input())
    changes = []
    graph = {i : [] for i in range(1, n + 1)}
    indegree = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split(" "))
        changes.append((a, b))
    for i in range(n):
        indegree[prev_ranks[i]] = i
        for j in range(i + 1, n):
            graph[prev_ranks[i]].append(prev_ranks[j])
    
    for b, a in changes:
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    
    stack = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            stack.append(i)
    answer = []
    
    find = 0
    for i in range(n):
        if len(stack) == 0:
            find = 1
            break
        elif len(stack) > 1:
            find = 2
            break
        cur_node = stack.pop()
        answer.append(cur_node)
        for next_node in graph[cur_node]:
            indegree[next_node] -= 1
            if indegree[next_node] < 1:
                stack.append(next_node)
    
    if find == 0:
        print(" ".join(list(map(str, answer))))
    elif find == 2:
        print("?")
    else:
        print("IMPOSSIBLE")