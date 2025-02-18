from collections import deque
N, K = map(int, input().split(" "))

queue = deque([(0, N)])
visit = set()
max_num = 100000
answer = -1
min_k = -1
while queue:
    cur_t, cur_x = queue.popleft()
    visit.add(cur_x)
    if cur_x == K:
        if min_k == -1 and answer == -1:
            answer = 1
            min_k = cur_t
        elif min_k == cur_t:
            answer += 1
    
    next_1 = cur_x - 1
    next_2 = cur_x + 1
    next_3 = cur_x * 2
    
    if next_1 not in visit and 0 <= next_1 <= max_num:
        queue.append((cur_t + 1, next_1))
    
    if next_2 not in visit and 0 <= next_2 <= max_num:
        queue.append((cur_t + 1, next_2))
    
    if next_3 not in visit and 0 <= next_3 <= max_num:
        queue.append((cur_t + 1, next_3))

print(min_k)
print(answer)