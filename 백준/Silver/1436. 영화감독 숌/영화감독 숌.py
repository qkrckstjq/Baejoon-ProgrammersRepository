N = int(input())
cnt = 0
num = 666
while cnt != N:
    num = str(num)
    if "666" in num:
        cnt += 1
    
    if cnt == N:
        print(num)
        break
    
    num = int(num)
    num += 1