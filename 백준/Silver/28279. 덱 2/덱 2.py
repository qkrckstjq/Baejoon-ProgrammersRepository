from collections import deque

N = int(input())
queue = deque()
answer = []
for _ in range(N):
    input_list = list(map(int, input().split(" ")))
    c = 0
    num = 0
    if len(input_list) == 2:
        num = input_list[1]
    c = input_list[0]
    
    if c == 1:
        queue.appendleft(num)
    elif c == 2:
        queue.append(num)
    elif c == 3:
        if queue:
            answer.append(queue.popleft())        
        else:
            answer.append(-1)
    elif c == 4:
        if queue:
            answer.append(queue.pop())        
        else:
            answer.append(-1)
    elif c == 5:
        answer.append(len(queue))
    elif c == 6:
        answer.append(0 if queue else 1)
    elif c == 7:
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif c == 8:
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)

[print(num) for num in answer]