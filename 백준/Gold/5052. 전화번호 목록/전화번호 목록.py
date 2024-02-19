# 2
# 3
# 911
# 97625999
# 91125426
# 5
# 113
# 12340
# 123440
# 12345
# 98346

import sys

def s_input():
    return sys.stdin.readline().strip()

T = int(s_input())
for _ in range(T):
    list_num = int(s_input())
    phone_num_list = []
    for _ in range(list_num):
        phone_number = s_input()
        phone_num_list.append(phone_number)
    phone_num_list.sort()
    find = False
    for i in range(0, len(phone_num_list) - 1):
        start_num = ""
        small_index = len(phone_num_list[i]) if len(phone_num_list[i]) < len(phone_num_list[i + 1]) else len(phone_num_list[i + 1])
        for j in range(small_index):
            start_num += phone_num_list[i + 1][j]
        if phone_num_list[i] == start_num:
            find = True
            break
    if find:
        print("NO")
    else:
        print("YES")