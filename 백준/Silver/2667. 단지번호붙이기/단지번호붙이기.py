import sys

move_y = [1, -1, 0, 0]
move_x = [0, 0, 1, -1]
def sInput():
    return sys.stdin.readline().strip()

def is_validate_range(arr, y, x):
    return 0 <= y < len(arr) and 0 <= x < len(arr)

def get_area(arr, visit, y, x):
    result = 1
    stack = [[y, x]]
    arr[y][x] = '0'
    while len(stack) != 0:
        cur = stack.pop()
        cur_y = cur[0]
        cur_x = cur[1]

        for i in range(4):
            next_y = cur_y + move_y[i]
            next_x = cur_x + move_x[i]
            if (is_validate_range(arr, next_y, next_x) and
                    not visit[next_y][next_x] and
                    arr[next_y][next_x] == '1'):
                result += 1
                visit[next_y][next_x] = True
                arr[next_y][next_x] = '0'
                stack.append([next_y, next_x])
    return result

T = int(sInput())

graph = []
visit = []
result = []
for i in range(T):
    row = list(sInput())
    graph.append(row)
    visit.append([False] * len(row))

for y in range(T):
    for x in range(T):
        if graph[y][x] == '1' and not visit[y][x]:
            result.append(get_area(graph, visit, y, x))
        visit[y][x] = True

print(len(result))
for area in sorted(result):
    print(area)