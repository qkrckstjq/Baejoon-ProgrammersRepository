import sys, heapq
from collections import deque, defaultdict

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())

arr = []
start_y = -1
start_x = -1
def set_start(i, arr):
    for j in range(len(arr)):
        if arr[j] == 9:
            return [i, j]
    return [-1, -1]
def can_move(arr, y, x, size):
    return True if 0 <= y < len(arr) and 0 <= x < len(arr) and size >= arr[y][x] else False
def get_dst(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)
def find_best(shark, arr):
    queue = deque()
    possibility = []
    visit = defaultdict(set)
    queue.append((shark['y'], shark['x'], 0))

    while queue:
        cur_y, cur_x, count = queue.popleft()
        if cur_x in visit[cur_y]:
           continue
        if arr[cur_y][cur_x] != 0 and arr[cur_y][cur_x] < shark['size']:
            possibility.append((cur_y, cur_x, count))
            continue
        visit[cur_y].add(cur_x)
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if can_move(arr, next_y, next_x, shark['size']):
                queue.append((next_y, next_x, count + 1))

    possibility.sort(key=lambda x: (x[2], x[0], x[1]))
    return possibility

def update_shark(shark, y, x):
    shark['eat'] += 1
    shark['y'] = y
    shark['x'] = x
    if shark['size'] == shark['eat']:
        shark['size'] += 1
        shark['eat'] = 0

for i in range(N):
    arr_x = list(map(int, s_input().split(" ")))
    if start_y == -1 and start_x == -1:
        start_y, start_x = set_start(i, arr_x)
    arr.append(arr_x)

arr[start_y][start_x] = 0
shark = {'y': start_y, 'x': start_x, 'size': 2, 'eat': 0}

result = 0
while True:
    possibility = find_best(shark, arr)
    if not possibility:
        break
    update_y = possibility[0][0]
    update_x = possibility[0][1]
    distance = possibility[0][2]
    result += distance
    arr[update_y][update_x] = 0
    update_shark(shark, update_y, update_x)

print(result)