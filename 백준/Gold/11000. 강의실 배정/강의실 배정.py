import heapq
import sys

def s_input():
    return sys.stdin.readline().strip()

T = int(s_input())
time_table = []
for i in range(T):
    start, end = list(map(int, s_input().split(" ")))
    time_table.append((start, end))
time_table.sort(key=lambda x: x[0])
heap = []
heapq.heappush(heap, time_table[0][1])

for i in range(1, T):
    if heap[0] > time_table[i][0]:
        heapq.heappush(heap, time_table[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time_table[i][1])
print(len(heap))
