#5
#1
#3
#8
#-2
#2

import sys

from collections import defaultdict

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
arr = []
hash_map = defaultdict(int)
for i in range(N):
    num = int(s_input())
    arr.append(num)
    hash_map[num] += 1

arr.sort()
frequency = sorted(hash_map, key=lambda x: (-hash_map[x], x))
avg = int(round(sum(arr) / N, 0))
mid = arr[N // 2]
min = frequency[0] if len(frequency) == 1 or hash_map[frequency[0]] != hash_map[frequency[1]] else frequency[1]
range = arr[-1] - arr[0]
print(avg)
print(mid)
print(min)
print(range)