from collections import deque
N, K = map(int, input().split(" "))
max_num = 100000
queue = deque([(0, N, f"{N}")])
visit = set([N])
while queue:
    cur_t, cur_x, cur_route = queue.popleft()
    
    if cur_x == K:
        print(cur_t)
        print(cur_route)
        break
    
    next_1 = cur_x - 1
    next_2 = cur_x + 1
    next_3 = cur_x * 2
    next_t = cur_t + 1
    
    if next_3 not in visit and 0 <= next_3 <= max_num:
        queue.append((next_t, next_3, cur_route + " " + str(next_3)))
        visit.add(next_3)
    
    if next_1 not in visit and 0 <= next_1 <= max_num:
        queue.append((next_t, next_1, cur_route + " " + str(next_1)))
        visit.add(next_1)
        
    if next_2 not in visit and 0 <= next_2 <= max_num:
        queue.append((next_t, next_2, cur_route + " " + str(next_2)))
        visit.add(next_2)