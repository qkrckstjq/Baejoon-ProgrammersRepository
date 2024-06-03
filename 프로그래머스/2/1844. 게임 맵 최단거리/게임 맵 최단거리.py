from collections import deque, defaultdict

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def check_range(y, x, base_y, base_x):
    return True if 0 <= y < base_y and 0 <= x < base_x else False

def check_possible(y, x, maps):
    return True if maps[y][x] != 0 else False

def solution(maps):
    len_y = len(maps)
    len_x = len(maps[0])
    q = deque()
    start = [0, 0, 0]
    q.append(start)
    # visit = defaultdict(set)
    maps[0][0] = 0
    while q:
        cur_y, cur_x, cur_v = q.popleft()
        # visit[cur_y].add(cur_x)
        if cur_y == len_y - 1 and cur_x == len_x - 1:
            return cur_v + 1
        
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            next_v = cur_v + 1
            # if check_range(next_y, next_x, len_y, len_x) and not next_x in visit[next_y] and check_possible(next_y, next_x, maps):
            #     q.append([next_y, next_x, next_v])
                
            if check_range(next_y, next_x, len_y, len_x) and check_possible(next_y, next_x, maps):
                maps[next_y][next_x] = 0
                q.append([next_y, next_x, next_v])
    
    return -1
    