from collections import deque

def solution(maps):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    s_y, s_x = 0, 0
    l_y, l_x = 0, 0
    e_y, e_x = 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                s_y = i
                s_x = j
            elif maps[i][j] == "L":   
                l_y = i
                l_x = j
            elif maps[i][j] == "E":
                e_y = i
                e_x = j
    
    def check_range(y, x):
        return True if 0 <= y < len(maps) and 0 <= x < len(maps[0]) else False
    
    def bfs(queue, e_y, e_x):
        visit = set()
        while queue:
            cur_y, cur_x, cur_k = queue.popleft()
            if cur_y == e_y and cur_x == e_x:
                return cur_k
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if check_range(next_y, next_x):
                    if maps[next_y][next_x] != "X" and (next_y, next_x) not in visit:
                        queue.append((next_y, next_x, cur_k + 1))
                        visit.add((next_y, next_x))
        return -1
    answer = 0
    
    lever_queue = deque()
    lever_queue.append((s_y, s_x, 0))
    answer += bfs(lever_queue, l_y, l_x)
    
    if answer == -1:
        return answer
    
    end_queue = deque()    
    end_queue.append((l_y, l_x, 0))
    v_e = bfs(end_queue, e_y, e_x)
    
    if v_e == -1:
        return v_e
    
    return answer + v_e