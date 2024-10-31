N = int(input())
works_time = sorted([list(map(int, input().split(" "))) for _ in range(N)], key=lambda x : x[1], reverse=True)
start_min = works_time[0][1]
for t, s in works_time:
    start_min = min((s - t), start_min - t)
        
print(-1 if start_min < 0 else start_min)