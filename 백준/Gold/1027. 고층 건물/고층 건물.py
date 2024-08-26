T = int(input())
buildings = list(map(int, input().split()))

answer = 0
for i in range(T):
    cur = 0
    for j in range(i + 1, T):
        if abs(i - j) == 1:
            cur += 1
            continue
        # y = ax + b
        x1, y1 = i, buildings[i]
        x2, y2 = j, buildings[j]
        
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
        
        possible = True
        for k in range(i + 1, j):
            x3, y3 = k, buildings[k]
            y = (x3 * a) + b
            if y <= y3:
                possible = False
                break
            
        if possible:
            cur += 1
            
    for j in range(i - 1, -1, -1):
        if abs(i - j) == 1:
            cur += 1
            continue
        # y = ax + b
        x1, y1 = i, buildings[i]
        x2, y2 = j, buildings[j]
        
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
        
        possible = True
        for k in range(i - 1, j, -1):
            x3, y3 = k, buildings[k]
            y = (x3 * a) + b
            if y <= y3:
                possible = False
                break
            
        if possible:
            cur += 1
            
    answer = max(cur, answer)
    

print(answer)