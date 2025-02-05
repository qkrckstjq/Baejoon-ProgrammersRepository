import heapq
N = int(input())

queue = []
answer = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if queue:
            answer.append(heapq.heappop(queue)[1])
        else:
            answer.append(0)
    else:
        heapq.heappush(queue, (abs(num), num))
[print(num) for num in answer]

    