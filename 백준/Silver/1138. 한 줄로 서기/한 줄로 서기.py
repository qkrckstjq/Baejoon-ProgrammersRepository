N = int(input())
memo = list(map(int, input().split(" ")))
answer = [False for _ in range(N)]

for i in range(N):
    j = 0
    cnt = 0
    while cnt < memo[i]:
        if answer[j] == False:
            cnt += 1
        j += 1

    while answer[j] != False:
        j += 1
    answer[j] = i + 1

result = ""
for w in answer:
    result += str(w)+" "
    
print(result)
