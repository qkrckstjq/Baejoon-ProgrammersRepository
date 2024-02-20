import heapq
import sys

def s_input():
    return sys.stdin.readline().strip()

T = int(s_input())
time_table = []
for i in range(T):
    start, end = list(map(int, s_input().split(" ")))
    time_table.append((start, end))
time_table.sort(key=lambda x: x[0]) #시작하는 시간순으로 정렬
heap = []
heapq.heappush(heap, time_table[0][1]) #첫번째 강의 끝나는 시간 힙에 넣기

for i in range(1, T):
    if heap[0] > time_table[i][0]:  #가장 빨리 끝나는 강의 시간이 시간표의i번째 시작 시간보다 크다면 시간표의 i번째 강의는 시작할수없음으로 새로운 강의실 필요
        heapq.heappush(heap, time_table[i][1])
    else: #가장 빨리 끝나는 시간이 시간표i번째 시작시간보다 작거나 같다면 하나의 강의실에서 진행이 가능함으로 힙에서 제거후 새롭게 갱신시켜줌
        heapq.heappop(heap)
        heapq.heappush(heap, time_table[i][1])
print(len(heap))
