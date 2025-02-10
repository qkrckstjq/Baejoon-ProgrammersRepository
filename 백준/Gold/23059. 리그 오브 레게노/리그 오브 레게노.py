from collections import defaultdict, deque
N = int(input())

graph = defaultdict(list)
indegree = {}

def dfs(graph, indegree, node):
    indegree[node] += 1
    for dst in graph[node]:
        dfs(graph, indegree, dst)

for _ in range(N):
    src, dst = input().split(" ")
    if src not in indegree:
        indegree[src] = 0
    if dst not in indegree:
        indegree[dst] = 1
    else:
        # dfs(graph, indegree, dst)
        indegree[dst] += 1
        
    graph[src].append(dst)

stack = []
visit = set()
for src in indegree.keys():
    if indegree[src] == 0:
        stack.append(src)
answer = []
# print(graph)
# print(indegree)

while stack:
    stack.sort(reverse=True)
    # print(stack)
    # print(indegree)
    cur_len = len(stack)
    temp = []
    for _ in range(cur_len):
        cur_src = stack.pop()
        answer.append(cur_src)
        for dst in graph[cur_src]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                temp.append(dst)
    stack.extend(temp)
    
if len(answer) == len(graph):
    [print(num) for num in answer]
else:
    print(-1)
    