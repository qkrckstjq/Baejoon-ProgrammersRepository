import sys

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def s_input():
    return sys.stdin.readline().strip()

def get_result(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            result += arr[i][j][0]
    return result + 2

def start_cleaning_upper(arr, cleaner_y1):
    arr[cleaner_y1 - 1][0] = [0, 0]
    for i in range(cleaner_y1 - 2, -1, -1):
        arr[i + 1][0] = arr[i][0]
    for i in range(0, len(arr[0]) - 1, 1):
        arr[0][i] = arr[0][i + 1]
    for i in range(1, cleaner_y1 + 1, 1):
        arr[i - 1][len(arr[0]) - 1] = arr[i][len(arr[0]) - 1]
    for i in range(len(arr[0]) - 1, 0, -1):
        arr[cleaner_y1][i] = arr[cleaner_y1][i - 1]
    arr[cleaner_y1][1] = [0, 0]

def start_cleaning_lower(arr, cleaner_y2):
    arr[cleaner_y2 + 1][0] = [0, 0]
    for i in range(cleaner_y2 + 2, len(arr), 1):
        arr[i - 1][0] = arr[i][0]
    for i in range(0, len(arr[0]) - 1, 1):
        arr[len(arr) - 1][i] = arr[len(arr) - 1][i + 1]
    for i in range(len(arr) - 1, cleaner_y2, -1):
        arr[i][len(arr[0]) - 1] = arr[i - 1][len(arr[0]) - 1]
    for i in range(len(arr[0]) - 1, 0, -1):
        arr[cleaner_y2][i] = arr[cleaner_y2][i - 1]
    arr[cleaner_y2][1] = [0, 0]

def check(arr, y, x):
    return False if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]) or arr[y][x][0] == -1 else True

def spreading(arr, y, x):
    repeat = 0
    if arr[y][x][0] < 5:
        return 0
    for k in range(4):
        next_y, next_x = y + dy[k], x + dx[k]
        if check(arr, next_y, next_x):
            arr[next_y][next_x][1] += arr[y][x][0] // 5
            repeat += 1
    arr[y][x][0] -= repeat * (arr[y][x][0] // 5)
    return repeat


def start_spread(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            spreading(arr, i, j)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j][0] += arr[i][j][1]
            arr[i][j][1] = 0




arr = []
y, x, t = list(map(int, s_input().split(" ")))

cleaner_y1 = 0
cleaner_y2 = 0
for i in range(y):
    arr_x = list(map(int, s_input().split(" ")))
    if arr_x[0] == -1:
        cleaner_y2 = i
    for i in range(len(arr_x)):
        arr_x[i] = [arr_x[i], 0]

    arr.append(arr_x)

cleaner_y1 = cleaner_y2 - 1

for i in range(t):
    start_spread(arr)
    start_cleaning_upper(arr, cleaner_y1)
    start_cleaning_lower(arr, cleaner_y2)

print(get_result(arr))

