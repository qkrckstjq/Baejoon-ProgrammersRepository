def solution(targets):
    targets.sort(key = lambda x:x[1])
    
    last_end = -1
    answer = 0
    for start, end in targets:
        if start >= last_end:
            answer += 1
            last_end = end
    
    return answer