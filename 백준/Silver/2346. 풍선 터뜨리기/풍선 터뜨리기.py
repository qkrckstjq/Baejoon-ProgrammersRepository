from collections import deque

N = int(input())
queue = deque(list(map(int, input().split(" "))))
for i in range(1, N + 1):
    queue[i - 1] = [queue[i - 1], i]
answer = []
while queue:
    answer.append(queue[0][1])
    # print(queue)
    num = queue[0][0]
    queue.popleft()
    if queue:
        if num > 0:
            for _ in range(num - 1):
                queue.append(queue.popleft())
        if num < 0:
            for _ in range(-num):
                queue.appendleft(queue.pop())

print(" ".join(list(map(str, answer))))