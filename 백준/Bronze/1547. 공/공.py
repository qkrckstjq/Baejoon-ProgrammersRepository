N = int(input())
q = 1

for _ in range(N):
    i, j = map(int, input().split(" "))
    if i == q:
        q = j
        continue
    if j == q:
        q = i

print(q)
    
