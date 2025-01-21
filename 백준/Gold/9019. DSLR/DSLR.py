from collections import deque

T = int(input())

def bfs(start, target):
    queue = deque([(start, "")])
    visit = [False for _ in range(10000)]
    visit[start] = True
    while queue:
        cur_num, cur_c = queue.popleft()
        if cur_num == target:
            print(cur_c)
            return
        
        next_d = cur_num * 2
        next_d = next_d % 10000 if next_d > 9999 else next_d
        if not visit[next_d]:
            visit[next_d] = True
            queue.append((next_d, cur_c + "D"))
            
        next_s = cur_num - 1
        next_s = 9999 if next_s < 0 else next_s
        if not visit[next_s]:
            visit[next_s] = True
            queue.append((next_s, cur_c + "S"))
        
        next_l = (cur_num % 1000) * 10 + cur_num // 1000
        if not visit[next_l]:
            visit[next_l] = True
            queue.append((next_l, cur_c + "L"))
        
        next_r = ((cur_num % 10) * 1000) + (cur_num // 10)
        if not visit[next_r]:
            visit[next_r] = True
            queue.append((next_r, cur_c + "R"))
            
for _ in range(T):
    start, target = map(int, input().split(" ")) 
    bfs(start, target)
