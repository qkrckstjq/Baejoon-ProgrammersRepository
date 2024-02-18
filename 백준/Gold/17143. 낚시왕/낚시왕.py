import sys
from collections import defaultdict

type = [-1, 0, 1, 2, 3]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
def s_input():
    return sys.stdin.readline().strip()
def is_possible(max, cur):
    return True if 0 <= cur < max else False
def get_next_yx(max_y, max_x, cur_y, cur_x, speed, direction):
    next_y = cur_y + (dy[type[direction]] * speed)
    next_x = cur_x + (dx[type[direction]] * speed)
    new_direction = direction
    if not is_possible(max_x, next_x):
        remain_move = abs(next_x) if next_x < 0 else next_x - (max_x - 1)
        repeat = remain_move // (max_x - 1)
        remain_after_repeat = remain_move - (max_x - 1) * repeat
        if repeat % 2 == 0: #남은 움직임을 반복한 횟수가 짝수 일 경우
            new_direction = 3 if next_x < 0 else 4
            next_x = remain_after_repeat if next_x < 0 else (max_x - 1) - remain_after_repeat
        else:
            new_direction = 4 if next_x < 0 else 3
            next_x = (max_x - 1) - remain_after_repeat if next_x < 0 else remain_after_repeat

    if not is_possible(max_y, next_y):
        remain_move = abs(next_y) if next_y < 0 else next_y - (max_y - 1)
        repeat = remain_move // (max_y - 1)
        remain_after_repeat = remain_move - (max_y - 1) * repeat
        if repeat % 2 == 0: #남은 움직임을 반복한 횟수가 짝수 일 경우
            new_direction = 2 if next_y < 0 else 1
            next_y = remain_after_repeat if next_y < 0 else (max_y - 1) - remain_after_repeat
        else:
            new_direction = 1 if next_y < 0 else 2
            next_y = (max_y - 1) - remain_after_repeat if next_y < 0 else remain_after_repeat

    return [next_y, next_x, new_direction]
def move_shark(shark_info, max_y, max_x, next_fisher):
    close_shark = 10000
    new_shark_info = defaultdict(dict)
    for y in list(shark_info.keys()):
        for x in list(shark_info[y]):
            shark = shark_info[y][x]
            next_y, next_x, new_direction = get_next_yx(max_y, max_x, y, x, shark['speed'], shark['direction'])
            if next_x in new_shark_info[next_y] and new_shark_info[next_y][next_x]['size'] < shark['size']:
                new_shark_info[next_y][next_x] = {'speed': shark['speed'], 'direction': new_direction, 'size': shark['size']}
            if not next_x in new_shark_info[next_y]:
                new_shark_info[next_y][next_x] = {'speed': shark['speed'], 'direction': new_direction, 'size': shark['size']}
            if next_x == next_fisher:
                close_shark = next_y if close_shark > next_y else close_shark
    return [new_shark_info, close_shark]

y, x, shark_num = list(map(int, s_input().split(" ")))
shark_info = defaultdict(dict)
close_shark = 10000
result = 0

for i in range(shark_num):
    shark_y, shark_x, speed, direction, size = list(map(int, s_input().split(" ")))
    shark_info[shark_y - 1][shark_x - 1] = {'speed': speed, 'direction': direction, 'size': size}
    if shark_x - 1 == 0:
        close_shark = shark_y - 1 if shark_y - 1 < close_shark else close_shark

for i in range(x):
    if close_shark != 10000:
        result += shark_info[close_shark][i]['size']
        del shark_info[close_shark][i]
    shark_info, close_shark = move_shark(shark_info, y, x, i + 1)

print(result)