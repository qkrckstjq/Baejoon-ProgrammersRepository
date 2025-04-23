from collections import deque
import heapq

N = int(input())

queue = []
heapq.heappush(queue, (0, 0, 0))

def growth(cur_h, num):
    if num == 1:
        return (cur_h + 1)
    elif num == 3:
        return (cur_h * 3)
    elif num == 5:
        return (cur_h ** 2)

visit = {0 : [0, 0]} #{높이 : [일수 : 물의 양]}

while queue:
    cur_h, cur_d, cur_w = heapq.heappop(queue)
    
    if cur_h == N:
        continue

    for w in [1, 3, 5]:
        next_h = growth(cur_h, w)
        next_d = cur_d + 1
        next_w = cur_w + w
        if next_h <= N:
            if (next_h not in visit) or (visit[next_h][0] >= next_d and visit[next_h][1] > next_w):
                visit[next_h] = [next_d, next_w]
                heapq.heappush(queue, (next_h, next_d, next_w))

print(visit[N][0], visit[N][1])
