import sys
from collections import deque, defaultdict
def s_input():
    return sys.stdin.readline().strip()

edge = int(s_input())
tree = defaultdict(list)
result = [0] * (edge + 1)

for _ in range(edge - 1):
    vertex1, vertex2 = list(map(int, (s_input().split(" "))))
    tree[vertex1].append(vertex2)
    tree[vertex2].append(vertex1)

stack = [1]
visit = set()
while stack:
    cur_node = stack.pop()
    visit.add(cur_node)
    for child in tree[cur_node]:
        if child not in visit:
            result[child] = cur_node
            stack.append(child)

for i in range(2, edge + 1, 1):
    print(result[i])