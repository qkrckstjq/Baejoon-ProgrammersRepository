from collections import deque

N, M = map(int, input().split(" "))
board = [0 for _ in range(101)]
ladder_graph = {}
for _ in range(N + M):
    src, dst = map(int, input().split(" "))
    ladder_graph[src] = dst
    

queue = deque()
queue.append((1, 0))
visit = set()
visit.add(1)
while queue:
    cur_node, cur_k = queue.popleft()
    if cur_node == 100:
        print(cur_k)
        break
    for i in range(1, 7):
        next_node = cur_node + i if (cur_node + i) not in ladder_graph else ladder_graph[cur_node + i]
        if next_node not in visit:
            queue.append((next_node, cur_k + 1))
            visit.add(next_node)