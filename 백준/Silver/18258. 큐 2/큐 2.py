from collections import deque
N = int(input())
queue = deque()
answer = []
for _ in range(N):
    input_list = list(input().split(" "))
    command = ""
    num = 0
    if len(input_list) == 2:
        num = input_list[1]
    command = input_list[0]
    
    if command == "push":
        queue.append(num)
    elif command == "pop":
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif command == "size":
        answer.append(len(queue))
    elif command == "empty":
        answer.append(0 if queue else 1)
    elif command == "front":
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif command == "back":
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)

[print(num) for num in answer]

