from collections import deque

def solution(priorities, location):
    # (우선순위, 인덱스) 형태의 튜플 리스트를 만듭니다.
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    
    answer = 0
    while True:
        # 큐의 첫 번째 요소를 꺼냅니다.
        front = queue.popleft()
        # 큐에서 가장 높은 우선순위를 찾습니다.
        if queue and max(queue, key=lambda x: x[0])[0] > front[0]:
            # 현재 문서보다 높은 우선순위가 존재하면 다시 큐의 뒤에 넣습니다.
            queue.append(front)
        else:
            # 그렇지 않으면 문서를 출력합니다.
            answer += 1
            # 만약 출력한 문서가 우리가 찾는 문서라면 반복을 종료합니다.
            if front[1] == location:
                break
            
    return answer
