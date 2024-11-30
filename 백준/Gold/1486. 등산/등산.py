# import heapq



# N, M, T, D = map(int, input().split(" "))
# board = []
# d = [[float('inf') for _ in range(M)] for _ in range(N)] #각 좌표별 도달할 수 있는 최소 시간
# d[0][0] = 0
# def check_range(y, x):
#     return True if 0 <= y < N and 0 <= x < M else False

# dy = [0, 0, 1, -1]
# dx = [1, -1, 0, 0]

# for _ in range(N):
#     row = list(input())
#     board.append(row)

# queue = []
# heapq.heappush(queue, (0, 0, 0))
# print(d)

# while queue:
#     cur_time, cur_y, cur_x = heapq.heappop(queue)
#     if d[cur_y][cur_x] < cur_time:
#         continue
#     for i in range(4):
#         next_y = cur_y + dy[i]
#         next_x = cur_x + dx[i]
#         if check_range(next_y, next_x): 
#             cur_h = ord(board[cur_y][cur_x])
#             next_h = ord(board[next_y][next_x])
#             dif = 0
#             if cur_h < next_h:
#                 dif = next_h - cur_h
#             else:
#                 dif = 1
#             total_time = cur_time + dif
#             if dif <= T and total_time < D and d[next_y][next_x] > total_time:
#                 d[next_y][next_x] = total_time
#                 heapq.heappush(queue, (total_time, next_y, next_x))

# # d = [[float('inf') for _ in range(M)] for _ in range(N)] #각 좌표별 도달할 수 있는 최소 시간
# result = ord(board[0][0])
# stack = []
# for i in range(N):
#     for j in range(M):
#         if i != 0 and j != 0 and d[i][j] != float('inf'):
#             heapq.heappush(stack, (d[i][j], i, j, ord(board[i][j])))
# print(stack)
# while stack:
#     cur_time, cur_y, cur_x, start_height = heapq.heappop(stack)
#     queue = []
#     heapq.heappush(queue, (cur_time, cur_y, cur_x))
#     d = [[float('inf') for _ in range(M)] for _ in range(N)]
#     d[cur_y][cur_x] = cur_time
#     while queue:
#         cur_time, cur_y, cur_x = heapq.heappop(queue)
        
#         if cur_y == 0 and cur_x == 0:
#             print("찾음", start_height, cur_time)
#             result = max(result, start_height)
#             break
        
#         if d[cur_y][cur_x] < cur_time:
#             continue
#         for i in range(4):
#             next_y = cur_y + dy[i]
#             next_x = cur_x + dx[i]
#             if check_range(next_y, next_x): 
#                 cur_h = ord(board[cur_y][cur_x])
#                 next_h = ord(board[next_y][next_x])
#                 dif = 0
#                 if cur_h < next_h:
#                     dif = next_h - cur_h
#                 else:
#                     dif = 1
#                 total_time = cur_time + dif
#                 if dif <= T and total_time <= D and d[next_y][next_x] > total_time:
#                     d[next_y][next_x] = total_time
#                     heapq.heappush(queue, (total_time, next_y, next_x))

# print(result)
    
import heapq

N, M, T, D = map(int, input().split(" "))
board = []
d = [[float('inf') for _ in range(M)] for _ in range(N)]  # 각 좌표별 도달할 수 있는 최소 시간
d[0][0] = 0

# 범위 체크 함수
def check_range(y, x):
    return 0 <= y < N and 0 <= x < M

# 높이 계산 함수
def height(c):
    if 'A' <= c <= 'Z':  # 'A'-'Z'는 0-25
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':  # 'a'-'z'는 26-51
        return ord(c) - ord('a') + 26

def get_time(next_h, cur_h):
    return (next_h - cur_h)**2

def check_t(next_h, cur_h):
    if abs(next_h - cur_h) <= T:
        return True
    return False

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 보드 입력
for _ in range(N):
    row = list(input())
    board.append(row)

queue = []
heapq.heappush(queue, (0, 0, 0))

while queue:
    cur_time, cur_y, cur_x = heapq.heappop(queue)
    if d[cur_y][cur_x] < cur_time:
        continue
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if check_range(next_y, next_x):
            cur_h = height(board[cur_y][cur_x])
            next_h = height(board[next_y][next_x])
            dif = get_time(next_h, cur_h)  # 높이 차이 계산
            total_time = cur_time + (dif if cur_h < next_h else 1)  # 높이 증가 시 거리 차이 반영
            if check_t(next_h, cur_h) and total_time <= D and d[next_y][next_x] > total_time:
                d[next_y][next_x] = total_time
                heapq.heappush(queue, (total_time, next_y, next_x))

result = height(board[0][0])
stack = []
for i in range(N):
    for j in range(M):
        if d[i][j] != float('inf'):
            heapq.heappush(stack, (d[i][j], i, j, height(board[i][j])))

# print(stack)
while stack:
    cur_time, cur_y, cur_x, start_height = heapq.heappop(stack)
    queue = []
    heapq.heappush(queue, (cur_time, cur_y, cur_x))
    d = [[float('inf') for _ in range(M)] for _ in range(N)]
    d[cur_y][cur_x] = cur_time
    while queue:
        cur_time, cur_y, cur_x = heapq.heappop(queue)
        if cur_y == 0 and cur_x == 0:
            # print(start_height)
            result = max(result, start_height)
            break
        if d[cur_y][cur_x] < cur_time:
            continue
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if check_range(next_y, next_x):
                cur_h = height(board[cur_y][cur_x])
                next_h = height(board[next_y][next_x])
                dif = get_time(next_h, cur_h)
                total_time = cur_time + (dif if cur_h < next_h else 1)
                if check_t(next_h, cur_h) and total_time <= D and d[next_y][next_x] > total_time:
                    # print(total_time, start_height)
                    d[next_y][next_x] = total_time
                    heapq.heappush(queue, (total_time, next_y, next_x))

print(result)
