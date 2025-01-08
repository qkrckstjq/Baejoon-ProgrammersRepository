from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    
    while progresses:
        num = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while progresses and progresses[0] >= 100:
            num += 1
            progresses.popleft()
            speeds.popleft()
        if num != 0:
            answer.append(num)
            
                
        
    
    return answer
