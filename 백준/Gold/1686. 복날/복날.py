from collections import deque

speed, time = map(float, input().split())
sy, sx = map(float, input().split())
dy, dx = map(float, input().split())

grid = [(sy, sx), (dy, dx)]
while True:
    try:
        line = input().strip()
        if not line:  # 빈 줄이 들어오면 종료
            break
        y, x = map(float, line.split())
        grid.append((y, x))
    except EOFError:  # 백준에서는 자동 처리됨
        break

def get_dst(y1, x1, y2, x2):
    return ((y1 - y2)**2 + (x1 - x2)**2) ** 0.5

graph = {}
for y, x in grid:
    graph[(y, x)] = []
    for i, j in grid:
        if y == i and x == j:
            continue
        else:
            if get_dst(y, x, i, j) <= (speed * time * 60):
                graph[(y, x)].append((i, j))

# print(graph)



def bfs(y, x):
    queue = deque([(y, x, 0)])
    visit = set()
    
    while queue:
        cur_y, cur_x, cur_cnt = queue.popleft()    
        if cur_y == dy and cur_x == dx:
            return cur_cnt
        for next_y, next_x in graph[(cur_y, cur_x)]:
            if not (next_y, next_x) in visit:
                visit.add((next_y, next_x))
                queue.append((next_y, next_x, cur_cnt + 1))
    return False
    

result = bfs(sy, sx)

if result:
    print(f"Yes, visiting {result - 1} other holes.")
else:
    print("No.")