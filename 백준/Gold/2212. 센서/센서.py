import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
K = int(s_input())
sensors = list(map(int, s_input().split(" ")))
sensors.sort()

distance = []
for i in range(len(sensors) - 1):
    distance.append(sensors[i + 1] - sensors[i])
distance.sort()
# print(distance)
# print(distance[:len(distance) - (K - 1)])
result = sum(distance[:N - K])
print(result)