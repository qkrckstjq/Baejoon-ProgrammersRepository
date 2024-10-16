v = int(input())
graph = dict()

for _ in range(v):
    input_list = list(map(int, input().split(" ")))
    src = input_list[0]
    graph[src] = {}
    for i in range(1, len(input_list) - 1, 2):
        if input_list[i] == -1:
            break
        graph[src][input_list[i]] = input_list[i + 1]

root = 1
stack = [[1, 0]]
visit = set()
answer = [0, 0]
while stack:
    cur_src, cur_v = stack.pop()
    if cur_src in visit:
        continue
    visit.add(cur_src)
    if answer[0] < cur_v:
        answer[0] = cur_v
        answer[1] = cur_src
    for dst, v in graph[cur_src].items():
        stack.append([dst, cur_v + v])

result = 0
stack = [[answer[1], 0]]
visit = set()
while stack:
    cur_src, cur_v = stack.pop()
    if cur_src in visit:
        continue
    visit.add(cur_src)
    result = max(result, cur_v)
    for dst, v in graph[cur_src].items():
        stack.append([dst, cur_v + v])

    
print(result)