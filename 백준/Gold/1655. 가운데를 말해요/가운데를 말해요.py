import sys
import heapq

input = sys.stdin.readline

n = int(input())
left, right = [], []

for _ in range(n):
    x = int(input())
    heapq.heappush(left, -x)

    if right and -left[0] > right[0]:
        heapq.heappush(right, -heapq.heappop(left))
        
    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    if len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))

    sys.stdout.write(f"{-left[0]}\n")