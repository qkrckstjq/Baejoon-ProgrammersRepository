import heapq

def solution(scoville, K):
    queue = []
    for s in scoville:
        heapq.heappush(queue, s)
    answer = 0
    
    while queue[0] < K:
        if len(queue) < 2:
            return -1
        first = heapq.heappop(queue)
        second = heapq.heappop(queue)
        new_s = (first + second * 2)
        heapq.heappush(queue, new_s)
        answer += 1
        
    return answer
