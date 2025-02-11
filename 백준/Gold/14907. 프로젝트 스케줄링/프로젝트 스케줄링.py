graph = {}
time_set = {}
indegree = {}
while True:
    try:
        node, *time_require = input().split(" ")
        time = 0
        require = []
        if len(time_require) == 2:
            time = time_require[0]
            require = list(time_require[1])
        else:
            time = time_require[0]
        for src in require:
            if src in graph:
                graph[src].append(node)
            else:
                graph[src] = [node]
                
        indegree[node] = len(require)
        time_set[node] = {"cur" : int(time), "prv" : 0}
    except:
        break

stack = [(node, 0) for node in indegree.keys() if indegree[node] == 0]
answer = 0
while stack:
    cur_node, prv_time = stack.pop()
    cur_time = time_set[cur_node]["prv"] + time_set[cur_node]["cur"]
    answer = max(answer, cur_time)
    if cur_node in graph:
        for next_node in graph[cur_node]:
            indegree[next_node] -= 1
            time_set[next_node]["prv"] = max(time_set[next_node]["prv"], cur_time)
            if indegree[next_node] == 0:
                stack.append((next_node, cur_time))
print(answer)
    
        