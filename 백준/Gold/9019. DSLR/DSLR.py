from collections import deque

T = int(input())

def bfs(start, target):
    queue = deque([(start, "")])
    visit = set()
    visit.add(start)
    while queue:
        cur_num, cur_c = queue.popleft()
        if cur_num == target:
            print(cur_c)
            return
        
        next_d = cur_num * 2
        next_d = next_d % 10000 if next_d > 9999 else next_d
        if next_d not in visit:
            visit.add(next_d)
            queue.append((next_d, f"{cur_c}D"))
            
        next_s = cur_num - 1
        next_s = 9999 if next_s < 0 else next_s
        if next_s not in visit:
            visit.add(next_s)
            queue.append((next_s, f"{cur_c}S"))
        
        next_l = (cur_num % 1000) * 10 + cur_num // 1000
        if next_l not in visit:
            visit.add(next_l)
            queue.append((next_l, f"{cur_c}L"))
        
        next_r = ((cur_num % 10) * 1000) + (cur_num // 10)
        if next_r not in visit:
            visit.add(next_r)
            queue.append((next_r, f"{cur_c}R"))
            
for _ in range(T):
    start, target = map(int, input().split(" ")) 
    bfs(start, target)
