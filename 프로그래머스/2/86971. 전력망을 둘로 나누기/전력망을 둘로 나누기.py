def dfs(graph, src):
    stack = [src]
    count = 0
    visit = set()
    while stack:
        cur_src = stack.pop()
        if not cur_src in visit:
            visit.add(cur_src)
            count += 1
            for child in graph[cur_src]:
                if not child in visit:
                    stack.append(child)
    return count

def solution(n, wires):
    graph = {}
    answer = n

    for s, d in wires:
        if s in graph:
            graph[s].append(d)
        else:
            graph[s] = [d]
        if d in graph:
            graph[d].append(s)
        else:
            graph[d] = [s]
    
    for s, d in wires:
        graph[s].remove(d)
        graph[d].remove(s)
        
        parent = dfs(graph, 1)
        child = n - parent

        answer = min(answer, abs(parent - child))
        
        graph[s].append(d)
        graph[d].append(s)
    
    return answer
