from collections import deque

N = int(input())
type_list = list(map(int, input().split(" ")))
init_list = list(map(int, input().split(" ")))
M = int(input())
values = list(map(int, input().split(" ")))

res = deque()

for i in range(N):
    if type_list[i] == 0:
        res.appendleft(init_list[i])
        
for i in range(M):
    res.append(values[i])
    print(res.popleft(), end=' ')