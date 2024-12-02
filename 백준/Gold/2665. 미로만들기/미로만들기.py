import heapq
N = int(input())
board = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def check_range(y, x):
    return True if 0 <= y < N and 0 <= x < N else False

d = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
d[0][0] = 0
for _ in range(N):
    row = list(map(int, input()))
    board.append(row)

queue = []
heapq.heappush(queue, (0, 0, 0))
while queue:
    cur_cnt, cur_y, cur_x = heapq.heappop(queue)    
    if d[cur_y][cur_x] < cur_cnt:
        continue
    
    if cur_y == N - 1 and cur_x == N - 1:
        print(cur_cnt)
        break
    
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if check_range(next_y, next_x):
            next_cnt = cur_cnt + (1 if board[next_y][next_x] == 0 else 0)
            if d[next_y][next_x] > next_cnt:
                # print(next_y, next_x)
                d[next_y][next_x] = next_cnt
                heapq.heappush(queue, (next_cnt, next_y, next_x))