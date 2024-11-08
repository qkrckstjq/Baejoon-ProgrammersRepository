N = int(input())
duplicate = {}
number = []
max_num = 0
for _ in range(N):
    num = int(input())
    max_num = max(num, max_num)
    number.append(num)
    if num in duplicate:
        duplicate[num] += 1
    else:
        duplicate[num] = 1
        
result = []
for n in number:
    ans = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans += 0 if i not in duplicate else duplicate[i]
            if i != n // i:
                ans += 0 if (n // i) not in duplicate else duplicate[n // i]
    result.append(ans - 1)
    

for ans in result:
    print(ans)