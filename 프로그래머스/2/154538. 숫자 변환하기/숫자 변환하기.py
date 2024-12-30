from collections import deque

def solution(x, y, n):
    answer = 0
    queue = deque()
    queue.append((x, 0))
    
    used = set()
    
    while queue:
        cur_v, cur_k = queue.popleft()
        if cur_v == y:
            return cur_k
        if (cur_v + n) not in used and cur_v + n <= y:
            used.add(cur_v + n)
            queue.append((cur_v + n, cur_k + 1))
        if (cur_v * 2) not in used and cur_v * 2 <= y:
            used.add(cur_v * 2)
            queue.append((cur_v * 2, cur_k + 1))
        if (cur_v * 3) not in used and cur_v * 3 <= y:
            used.add(cur_v * 3)
            queue.append((cur_v * 3, cur_k + 1))
    return -1