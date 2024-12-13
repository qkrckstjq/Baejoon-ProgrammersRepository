import copy
from collections import deque

def solution(maze):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    def check_range(y, x, d_y, d_x):
        return True if (0 <= y < len(maze) and 0 <= x < len(maze[0])) and (y != d_y or x != d_x) and maze[y][x] != 5 else False
    
    r_start = [0, 0]
    b_start = [0, 0]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                r_start = [i, j]
            elif maze[i][j] == 2:
                b_start = [i, j]
    
    queue = deque()
    r_visit = set()
    b_visit = set()
    r_visit.add((r_start[0], r_start[1]))
    b_visit.add((b_start[0], b_start[1]))
    queue.append([r_start, b_start, r_visit, b_visit, 0])
    
    answer = 0
    while queue:
        red, blue, r_visit, b_visit, cnt = queue.popleft()
        r_y, r_x = red
        b_y, b_x = blue
        r_in_goal = maze[r_y][r_x] == 3
        b_in_goal = maze[b_y][b_x] == 4
        if r_in_goal and b_in_goal:
            answer = cnt
            break
        if not r_in_goal and not b_in_goal:
            for i in range(4):
                next_r_y = r_y + dy[i]
                next_r_x = r_x + dx[i]
                if check_range(next_r_y, next_r_x, b_y, b_x) and (next_r_y, next_r_x) not in r_visit :
                    copy_r_visit = copy.deepcopy(r_visit)
                    copy_r_visit.add((next_r_y, next_r_x))
                    for j in range(4):
                        next_b_y = b_y + dy[j]
                        next_b_x = b_x + dx[j]
                        if check_range(next_b_y, next_b_x, next_r_y, next_r_x) and (next_b_y, next_b_x) not in b_visit:
                            copy_b_visit = copy.deepcopy(b_visit)
                            copy_b_visit.add((next_b_y, next_b_x))
                            queue.append([[next_r_y, next_r_x], [next_b_y, next_b_x], copy.deepcopy(copy_r_visit), copy.deepcopy(copy_b_visit), cnt + 1])
            for i in range(4):
                next_b_y = b_y + dy[i]
                next_b_x = b_x + dx[i]
                if check_range(next_b_y, next_b_x, r_y, r_x) and (next_b_y, next_b_x) not in b_visit :
                    copy_b_visit = copy.deepcopy(b_visit)
                    copy_b_visit.add((next_b_y, next_b_x))
                    for j in range(4):
                        next_r_y = r_y + dy[j]
                        next_r_x = r_x + dx[j]
                        if check_range(next_r_y, next_r_x, next_b_y, next_b_x) and (next_r_y, next_r_x) not in r_visit:
                            copy_r_visit = copy.deepcopy(r_visit)
                            copy_r_visit.add((next_r_y, next_r_x))
                            queue.append([[next_r_y, next_r_x], [next_b_y, next_b_x], copy.deepcopy(copy_r_visit), copy.deepcopy(copy_b_visit), cnt + 1])
        elif not r_in_goal and b_in_goal:
            for i in range(4):
                next_r_y = r_y + dy[i]
                next_r_x = r_x + dx[i]
                if check_range(next_r_y, next_r_x, b_y, b_x) and (next_r_y, next_r_x) not in r_visit :
                    copy_r_visit = copy.deepcopy(r_visit)
                    copy_r_visit.add((next_r_y, next_r_x))
                    queue.append([[next_r_y, next_r_x], [b_y, b_x], copy.deepcopy(copy_r_visit), copy.deepcopy(b_visit), cnt + 1])
        elif not b_in_goal and r_in_goal:
            for i in range(4):
                next_b_y = b_y + dy[i]
                next_b_x = b_x + dx[i]
                if check_range(next_b_y, next_b_x, r_y, r_x) and (next_b_y, next_b_x) not in b_visit:
                    copy_b_visit = copy.deepcopy(b_visit)
                    copy_b_visit.add((next_b_y, next_b_x))
                    queue.append([[r_y, r_x], [next_b_y, next_b_x], copy.deepcopy(r_visit), copy.deepcopy(copy_b_visit), cnt + 1])
        if not queue:
            answer = 0
    return answer