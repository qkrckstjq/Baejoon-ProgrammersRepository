import sys
from collections import defaultdict
def s_input():
    return sys.stdin.readline().strip()
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def print_field(field):
    for row in field:
        print(row)
def is_possible(y, x):
    return True if 0 <= y < 12 and 0 <= x < 6 else False
def pull_down(field):
    for x in range(6):
        bottom = find_bottom(field, x)
        next_color = find_color(field, bottom, x)
        while bottom >= 0 and next_color >= 0:
            field[bottom][x] = field[next_color][x]
            field[next_color][x] = '.'
            bottom -= 1
            next_color = find_color(field, bottom, x)
def find_color(field, y, x):
    next_color = y
    while field[next_color][x] == '.' and next_color >= 0:
        next_color -= 1
    return next_color
def find_bottom(field, x):
    bottom = 11
    while field[bottom][x] != '.' and bottom >= 0:
        bottom -= 1
    return bottom
def find_next(field, visit):
    for y in range(11, -1, -1):
        for x in range(6):
            if field[y][x] != '.' and not x in visit[y]:
                visit[y].add(x)
                return [y, x]
    return [-1, -1]
def remove_all_possibility(field):
    visit = defaultdict(set)
    start_y, start_x = find_next(field, visit)
    result = 0
    while start_y != -1 and start_x != -1:
        delete_success = False
        while start_y != -1 and start_x != -1:
            if dfs(field, start_y, start_x, visit):
                delete_success = True
                visit = defaultdict(set)
            start_y, start_x = find_next(field, visit)
        result += 1 if delete_success else 0
        pull_down(field)
        start_y, start_x = find_next(field, visit)
    return result
def dfs(field, start_y, start_x, total_visit):
    color = field[start_y][start_x]
    stack = [[start_y, start_x]]
    memo = [[start_y, start_x]]
    visit = defaultdict(set)
    count = 0

    while stack:
        cur_y, cur_x = stack.pop()
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if is_possible(next_y, next_x) and not next_x in visit[next_y] and field[next_y][next_x] == color:
                total_visit[next_y].add(next_x)
                stack.append([next_y, next_x])
                memo.append([next_y, next_x])
                visit[next_y].add(next_x)
                count += 1
    if count >= 4:
        for y, x in memo:
            field[y][x] = '.'
        return True
    return False

field = [] * 12
result = 0
for i in range(12):
    info = list(s_input())
    field.append(info)
print(remove_all_possibility(field))