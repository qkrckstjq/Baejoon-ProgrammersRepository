from collections import deque
T = int(input())
dy = [1, 1, -1, -1, 2, 2, -2, -2]
dx = [-2, 2, -2, 2, -1, 1, 1, -1]
for _ in range(T):
    N = int(input())
    board = [[False for _ in range(N)] for _ in range(N)]
    start_y, start_x = map(int, input().split(" "))
    end_y, end_x = map(int, input().split(" "))
    queue = deque([(start_y, start_x, 0)])
    while queue:
        cur_y, cur_x, cur_k = queue.popleft()
        if cur_y == end_y and cur_x == end_x:
            print(cur_k)
            break
        for i in range(8):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0 <= next_y < N and 0 <= next_x < N:
                if not board[next_y][next_x]:
                    board[next_y][next_x] = True
                    queue.append((next_y, next_x, cur_k + 1))
        
                