def solution(k, dungeons):    
    answer = -1
    stack = [[0, 0, k, set()]]
    while stack:
        cur_i, count, cur_k, visit = stack.pop()
        min_v = dungeons[cur_i][0]
        use_v = dungeons[cur_i][1]
        answer = max(count, answer)
        for i in range(len(dungeons)):
            if not i in visit and cur_k >= dungeons[i][0]:
                new_visit = visit.copy()
                new_visit.add(i)
                stack.append([i, count + 1, cur_k - dungeons[i][1], new_visit])
                
    return answer