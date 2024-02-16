import sys
from collections import defaultdict, deque
def s_input():
    return sys.stdin.readline().strip()

vertex, edge, start = list(map(int, s_input().split(" ")))

graph = defaultdict(list)
for i in range(edge):
    src, dst = list(map(int, s_input().split(" ")))
    graph[src].append(dst)
    graph[dst].append(src)

for src in list(graph.keys()):
    graph[src].sort()

visit_dfs = set()
visit_bfs = set()

stack = [start]
queue = deque()
queue.append(start)

dfs = []
bfs = []

while stack or queue:
    if stack:
        cur_node = stack.pop()
        if cur_node in visit_dfs:
            continue
        visit_dfs.add(cur_node)
        dfs.append(str(cur_node))
        for i in range(len(graph[cur_node]) - 1, -1, -1):
            stack.append(graph[cur_node][i])
    if queue:
        cur_node = queue.popleft()
        if cur_node in visit_bfs:
            continue
        visit_bfs.add(cur_node)
        bfs.append(str(cur_node))
        for next in graph[cur_node]:
            queue.append(next)

print(' '.join(dfs))
print(' '.join(bfs))