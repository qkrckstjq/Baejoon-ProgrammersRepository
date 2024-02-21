# import sys
#
# def s_input():
#     return sys.stdin.readline().strip()
#
# def cut(arr, target):
#     result = 0
#     for value in arr:
#         if value > target:
#             result += (value - target)
#     return result
#
# N, M = list(map(int, s_input().split(" ")))
# trees = list(map(int, s_input().split(" ")))
# min_v = 1
# max_v = max(trees)
#
# while min_v <= max_v:
#     mid_v = (min_v + max_v) // 2
#     cut_v = cut(trees, mid_v)
#     # if cut_v == M:
#     #     print(mid_v)
#     #     break
#     if cut_v < M:
#         max_v = mid_v - 1
#     else:
#         min_v = mid_v + 1
# print(max_v)

import sys

def s_input():
    return sys.stdin.readline().strip()

def get_nums(arr, base):
    result = 0
    for cable in arr:
        result += cable // base
    return result

K, N = list(map(int, s_input().split(" ")))
min_v = 1
max_v = 0
lan_cables = []
for i in range(K):
    lan_cable = int(s_input())
    lan_cables.append(lan_cable)
    max_v = max(lan_cable, max_v)

while min_v <= max_v:
    mid_v = (min_v + max_v) // 2
    cable_num = get_nums(lan_cables, mid_v)
    if cable_num < N:
        max_v = mid_v - 1
    else:
        min_v = mid_v + 1

print(max_v)