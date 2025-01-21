from collections import deque

T = int(input())

def bfs(start, target):
    queue = deque([(int(start), "")])  # 숫자와 경로만 저장
    visit = set()
    visit.add(int(start))
    
    while queue:
        cur_num, cur_c = queue.popleft()
        if cur_num == int(target):
            print(cur_c)
            return
        
        # D 연산
        next_d = (cur_num * 2) % 10000
        if next_d not in visit:
            visit.add(next_d)
            queue.append((next_d, cur_c + "D"))
        
        # S 연산
        next_s = cur_num - 1 if cur_num > 0 else 9999
        if next_s not in visit:
            visit.add(next_s)
            queue.append((next_s, cur_c + "S"))
        
        # L 연산
        cur_str = f"{cur_num:04d}"  # 4자리 문자열로 변환
        next_l = int(cur_str[1:] + cur_str[0])  # 왼쪽 시프트
        if next_l not in visit:
            visit.add(next_l)
            queue.append((next_l, cur_c + "L"))
        
        # R 연산
        next_r = int(cur_str[-1] + cur_str[:-1])  # 오른쪽 시프트
        if next_r not in visit:
            visit.add(next_r)
            queue.append((next_r, cur_c + "R"))

for _ in range(T):
    start, target = input().split()
    bfs(start, target)
