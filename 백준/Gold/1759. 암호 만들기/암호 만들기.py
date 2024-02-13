import sys
from collections import deque

vowel = set(["a", "e", "i", "o", "u"])


def s_input():
    return sys.stdin.readline().strip()


def check(str):
    v_number = 0
    c_number = 0
    for c in str:
        if c in vowel:
            v_number += 1
        else:
            c_number += 1
    return True if v_number >= 1 and c_number >= 2 else False


L, C = list(map(int, s_input().split(" ")))
sorted_words = sorted(s_input().split(" "))

result = []
queue = deque()

for i in range(0, C - L + 1, 1):
    queue.append((sorted_words[i], i))

while queue:
    cur_str, index = queue.popleft()
    if len(cur_str) == L and check(cur_str):
        print(cur_str)
        continue
    if len(cur_str) >= L:
        continue
    for i in range(index + 1, C, 1):
        next_str = cur_str + sorted_words[i]
        queue.append((next_str, i))

