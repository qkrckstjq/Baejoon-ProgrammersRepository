def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    count = 0
    
    for i in new_lost:
        if (i - 1) in new_reserve:
            new_reserve.remove(i - 1)
            count += 1
        elif (i + 1) in new_reserve:
            new_reserve.remove(i + 1)
            count += 1
            
    answer = len(new_lost) - count
    
    return n - answer