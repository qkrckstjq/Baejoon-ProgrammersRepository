def solution(n, wires):
    graph = {}
    
    for s, d in wires:
        if s in graph:
            graph[s].append(d)
        else:
            graph[s] = [d]
        if d in graph:
            graph[d].append(s)
        else:
            graph[d] = [s]
    print(graph)
    
    answer = -1
    return answer