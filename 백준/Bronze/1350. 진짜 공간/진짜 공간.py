N = int(input())
result = 0
mem_list = list(map(int, input().split(" ")))
cluster = int(input())
for mem in mem_list:
    if mem == 0:
        continue
    elif mem % cluster == 0:
        result += (cluster * (mem // cluster))
    else:
        result += (cluster * (mem // cluster + 1))

print(result)