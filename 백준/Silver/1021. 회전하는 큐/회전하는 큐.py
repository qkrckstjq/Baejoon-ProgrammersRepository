from collections import deque

def find_target(queue, target):
    for i in range(len(queue)):
        if target == queue[i]:
            return i

N, M = list(map(int, input().split(" ")))
targets = list(map(int, input().split(" ")))
queue = deque(range(1, N + 1))
answer = 0

for target in targets:
    idx = find_target(queue, target)
    left = idx
    right = len(queue) - idx
    if left <= right:
        answer += left
        for j in range(left):
            temp = queue.popleft()
            queue.append(temp)
    if left > right:
        answer += right
        for j in range(right):
            temp = queue.pop()
            queue.appendleft(temp)
    
    queue.popleft()

print(answer)