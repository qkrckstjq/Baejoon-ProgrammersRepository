import sys
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()


node_num = int(s_input())
tree = list(map(int, (s_input().split(" "))))
tree_graph = defaultdict(list)
delete_node = int(s_input())
root_node = 0
for i in range(node_num):
    if tree[i] == -1:
        root_node = i
        continue
    else:
        tree_graph[tree[i]].append(i)

result = 0
stack = [root_node]
while stack:
    cur_node = stack.pop()
    if cur_node == delete_node:
        continue
    childrens = tree_graph[cur_node]
    if len(childrens) == 0:
        result += 1
    else:
        for child in childrens:
            if len(childrens) == 1 and child == delete_node:
                result += 1
            stack.append(child)

print(result)