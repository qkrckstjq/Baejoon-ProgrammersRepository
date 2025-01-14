N = int(input())

max_y, max_x = -float('inf'), -float('inf')
min_y, min_x = float('inf'), float('inf')

for _ in range(N):
    y, x = map(int, input().split(" "))
    max_y = max(max_y, y)
    max_x = max(max_x, x)
    
    min_y = min(min_y, y)
    min_x = min(min_x, x)
    
y = max_y - min_y
x = max_x - min_x

print(y * x)