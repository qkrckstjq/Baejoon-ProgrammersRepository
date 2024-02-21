import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
time_table = []
for i in range(N):
    hour, minute, sec = list(map(int, s_input().split(" ")))
    time_table.append((hour, minute, sec))

time_table.sort(key=lambda x:(x[0], x[1], x[2]))
for i in range(N):
    result = str(time_table[i][0]) + " " + str(time_table[i][1]) + " " + str(time_table[i][2])
    print(result)