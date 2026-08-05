def solution(n, lost, reserve):
    answer = 0
    lost_s = set(lost)
    reserve_d = set(reserve)
    for l in lost:
        if l in reserve_d:
            lost_s.remove(l)
            reserve_d.remove(l)
    
    for i in range(1, n + 1):
        if not i in lost_s:
            answer += 1
            continue
            
        if i in lost_s:
            front = i - 1
            back = i + 1
            if front in reserve_d:
                answer += 1
                reserve_d.remove(front)
                continue
                
            if back in reserve_d:
                answer += 1
                reserve_d.remove(back)
                continue
                
    return answer