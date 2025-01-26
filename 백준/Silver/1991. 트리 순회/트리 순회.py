from collections import deque
v = int(input())
tree = {}

for _ in range(v):
    src, *dst_list = input().split(" ")
    tree[src] = []
    for dst in dst_list:
        tree[src].append(dst)

stack = []
stack_mid = []
queue = deque()

def dfs(node, arr):
    if node == ".":
        return
    arr.append(node)
    for dst in tree[node]:
        dfs(dst, arr)
        
def dfs_mid(node, arr):
    if node == ".":
        return
    dfs_mid(tree[node][0], arr)
    arr.append(node)
    dfs_mid(tree[node][1], arr)    
            
def dfs_1(node, arr):
    if node == ".":
        return
    for dst in tree[node]:
        dfs_1(dst, arr)
    arr.append(node)
    


dfs("A", stack)
dfs_mid("A", stack_mid)
dfs_1("A", queue)

print("".join(stack))
print("".join(stack_mid))
print("".join(queue))