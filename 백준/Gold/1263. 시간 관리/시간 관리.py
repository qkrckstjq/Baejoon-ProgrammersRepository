import heapq

def latest_start_time(N, tasks):
    tasks.sort(key=lambda x: x[1], reverse=True)

    start_time = tasks[0][1]
    
    for t, s in tasks:
        start_time = min(start_time, s)  
        start_time -= t  
        
        if start_time < 0:
            return -1

    return start_time

N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
print(latest_start_time(N, tasks))