L = int(input().strip())
S = list(map(int, input().split()))
n = int(input().strip())

S.sort()

if n in S:
    print(0)
    exit()

lower = 0        
upper = None     

for x in S:
    if x < n:
        lower = x
    elif x > n:
        upper = upper or x
        break

if upper is None:
    print(0)
    exit()

start = lower + 1
end = upper - 1
if start > end:
    print(0)
else:
    ans = (n - start) * (end - n + 1) + (end - n)
    print(ans)