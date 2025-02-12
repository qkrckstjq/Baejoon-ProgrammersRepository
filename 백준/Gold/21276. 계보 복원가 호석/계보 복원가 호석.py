N = int(input())
names = list(input().split(" "))
graph = {name : [] for name in names}
indegree = {name : 0 for name in names}
M = int(input())
for _ in range(M):
    child, parent = list(input().split(" "))
    graph[parent].append(child)
    indegree[child] += 1
    
k_list = []
stack = []
child_graph = {}
for name in indegree.keys():
    if indegree[name] == 0:
        stack.append(name)
# print("\n")
# print(indegree)
# print(graph)
# print("\n")
print(len(stack))
stack.sort()
print(" ".join(stack))
while stack:
    cur_name = stack.pop()
    k_list.append(cur_name)
    child_graph[cur_name] = []
    for child in graph[cur_name]:
        indegree[child] -= 1
        if indegree[child] == 0:
            stack.append(child)
            child_graph[cur_name].append(child)
k_list.sort()     
for name in k_list:
    child_len = len(child_graph[name])
    child_graph[name].sort()
    childrens = " ".join(child_graph[name])
    print(f"{name} {child_len} {childrens}")



# print(graph)
# print(indegree)