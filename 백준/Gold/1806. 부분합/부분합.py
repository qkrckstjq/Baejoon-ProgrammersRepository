N, target = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

answer = float('inf')
start, cur_sum = 0, 0
for i in range(N):
    cur_sum += arr[i]
    
    while cur_sum >= target:
        answer = min(answer, i - start + 1)
        cur_sum -= arr[start]
        start += 1

if answer == float('inf'):
    print(0)
else:
    print(answer)