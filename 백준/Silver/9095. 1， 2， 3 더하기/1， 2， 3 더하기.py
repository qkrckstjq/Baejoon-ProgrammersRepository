import sys


def s_input():
    return sys.stdin.readline().strip()


default_list = [1, 2, 3]

T = int(s_input())
for _ in range(T):
    target_number = int(s_input())
    stack = [3, 2, 1]
    result = 0
    while stack:
        cur_number = stack.pop()
        if cur_number == target_number:
            result += 1
            continue
        if cur_number > target_number:
            continue
        for default_number in default_list:
            next_number = default_number + cur_number
            stack.append(next_number)
    print(result)
