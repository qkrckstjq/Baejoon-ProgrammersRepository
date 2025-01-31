from collections import deque

N = int(input())
queue = deque(list(map(int, input().split())))
stack = []
current = 1

while queue or stack:
    if queue and queue[0] == current:  # queue에서 올바른 번호가 나왔을 때
        queue.popleft()
        current += 1
    elif stack and stack[-1] == current:  # stack에서 올바른 번호가 나왔을 때
        stack.pop()
        current += 1
    elif queue:  # stack으로 옮겨야 하는 경우
        stack.append(queue.popleft())
    else:  # 더 이상 진행할 수 없는 경우
        print("Sad")
        break
else:
    print("Nice")
