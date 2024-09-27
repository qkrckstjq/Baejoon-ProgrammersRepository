t = int(input())

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(graph, y, x):
    stack = [[y, x]]
    graph[y].remove(x)
    while stack:
        cur_y, cur_x = stack.pop()
        
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if next_y in graph and next_x in graph[next_y]:
                stack.append([next_y, next_x])
                graph[next_y].remove(next_x)
                
        

for i in range(t):
    m, n, k = list(map(int, input().split(" ")))
    graph = dict()
    for j in range(k):
        x, y = list(map(int, input().split(" ")))
        if y in graph:
            graph[y].add(x)
        else:
            graph[y] = {x}
    
    answer = 0
    for j in range(n):
        for q in range(m):
            if j in graph and q in graph[j]:
                dfs(graph, j, q)
                answer += 1
    
    print(answer)