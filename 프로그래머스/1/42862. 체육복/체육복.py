def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    to_remove = set()  # 제거할 요소를 저장할 집합
    
    for i in new_lost:
        if (i - 1) in new_reserve:
            to_remove.add(i)
            new_reserve.remove(i - 1)
        elif (i + 1) in new_reserve:
            to_remove.add(i)
            new_reserve.remove(i + 1)
    
    new_lost -= to_remove  # 반복문이 끝난 후 제거
    
    return n - len(new_lost)
