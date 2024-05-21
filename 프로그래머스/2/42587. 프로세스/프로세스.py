from collections import deque;

def solution(priorities, location):
    index_list = []
    
    for i in range(len(priorities)):
        temp = [priorities[i], i]
        index_list.append(temp)
        
    queue = deque(index_list)
    
    answer = 0
    while True:
        front = queue.popleft()
        if queue and max(queue, key=lambda x:x[0])[0] > front[0]:
            queue.append(front)
        elif front[1] == location:
            break
        else:
            answer += 1
            
            
    return answer + 1