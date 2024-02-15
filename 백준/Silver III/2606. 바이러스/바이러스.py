import sys


def sInput():
    return sys.stdin.readline().strip()


computers = int(sInput())
vertex_num = int(sInput())
graph = dict()
visit = dict()

for i in range(vertex_num):
    vertex = sInput().split(" ")
    src = vertex[0]
    dst = vertex[1]
    visit[src] = False
    visit[dst] = False
    if src in graph:
        graph[src].append(dst)
    else:
        graph[src] = [dst]
    if dst in graph:
        graph[dst].append(src)
    else:
        graph[dst] = [src]


result = 0
stack = ['1']
visit['1'] = True
while len(stack) != 0:
    cur_src = stack.pop()
    if cur_src in graph:
        for next_src in graph[cur_src]:
            if not visit[next_src]:
                visit[next_src] = True
                stack.append(next_src)
                result += 1

print(result)
