import sys
from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

graph = defaultdict(dict)
N, M = list(map(int, s_input().split(" ")))
for _ in range(N - 1):
    src, dst, w = list(map(int, s_input().split(" ")))
    graph[src][dst] = w
    graph[dst][src] = w

for _ in range(M):
    src, dst = list(map(int, s_input().split(" ")))
    stack = [(src, 0)]
    visit = set()
    while stack:
        cur_src, cur_w = stack.pop()
        if cur_src == dst:
            print(cur_w)
            break
        if cur_src in visit:
            continue
        visit.add(cur_src)
        for next_dst, w in graph[cur_src].items():
            next_w = cur_w + w
            stack.append((next_dst, next_w))