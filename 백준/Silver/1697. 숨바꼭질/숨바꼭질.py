from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
else:
    queue = deque([(N, 0)])  # (현재 위치, 시간)
    used = set([N])  # 시작 위치는 방문 처리
    
    while queue:
        cur_n, cur_t = queue.popleft()
        
        # 목표 위치 도달 시 종료
        if cur_n == K:
            print(cur_t)
            break
        
        # 다음 가능한 위치 추가
        for next_n in (cur_n * 2, cur_n + 1, cur_n - 1):
            if 0 <= next_n <= 100000 and next_n not in used:  # 유효 범위 내에서만 탐색
                used.add(next_n)  # 방문 처리
                queue.append((next_n, cur_t + 1))
