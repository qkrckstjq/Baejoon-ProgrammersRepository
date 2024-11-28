N = int(input())
result = []
stack = []

def dfs():
    for num in range(0, 10):
        if len(stack) == 0 or stack[-1] > num:
            stack.append(num)
            join_num = int("".join(list(map(str, stack))))
            result.append(join_num)
            dfs()
            stack.pop()
            
dfs()
result.sort()
try:
    print(result[N])
except:
    print(-1)