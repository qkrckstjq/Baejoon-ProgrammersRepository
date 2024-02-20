import sys, heapq

def s_input():
    return sys.stdin.readline().strip()

T = int(s_input())
for _ in range(T):
    K = int(s_input())
    files = list(map(int, s_input().split(" ")))
    heapq.heapify(files)
    result = 0
    for _ in range(K - 1):
        c1 = heapq.heappop(files)
        c2 = heapq.heappop(files)
        x1 = c1 + c2
        result += x1
        heapq.heappush(files, x1)
    print(result)

