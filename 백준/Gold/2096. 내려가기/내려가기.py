import sys
input = sys.stdin.readline

n = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for i in range(1, n):
    cur = list(map(int, input().split()))

    cur_max = [
        cur[0] + max(prev_max[0], prev_max[1]),
        cur[1] + max(prev_max[0], prev_max[1], prev_max[2]),
        cur[2] + max(prev_max[1], prev_max[2])
    ]

    cur_min = [
        cur[0] + min(prev_min[0], prev_min[1]),
        cur[1] + min(prev_min[0], prev_min[1], prev_min[2]),
        cur[2] + min(prev_min[1], prev_min[2])
    ]

    prev_max, prev_min = cur_max, cur_min

maxVal, minVal = max(prev_max), min(prev_min)
print(maxVal, minVal)