from collections import deque
N, K = map(int, input().split(" "))
visit = set()
queue = deque([(0, N)])
max_num = 100000
while queue:
    cur_k, cur_x = queue.popleft()
    visit.add(cur_x)
    if cur_x == K:
        print(cur_k)
        break
    next_1 = cur_x - 1
    next_2 = cur_x + 1
    next_3 = cur_x * 2
    if next_3 not in visit and 0 <= next_3 <= max_num:
        queue.appendleft((cur_k, next_3))
    
    if next_1 not in visit and 0 <= next_1 <= max_num:
        queue.append((cur_k + 1, next_1))
    
    if next_2 not in visit and 0 <= next_2 <= max_num:
        queue.append((cur_k + 1, next_2))