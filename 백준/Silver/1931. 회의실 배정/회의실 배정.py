import sys


def s_input():
    return sys.stdin.readline().strip()


N = int(s_input())
time_table = []
for i in range(N):
    start, end = list(map(int, s_input().split(" ")))
    time_table.append((start, end))

time_table.sort(key=lambda x:(x[1], x[0]))
result = 1
before_end = time_table[0][1]
for i in range(1, N):
    start, end = time_table[i]
    if before_end <= start:
        result += 1
        before_end = end

print(result)