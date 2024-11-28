N = int(input())

result = []
stack = []
# for i in range(0, 10):
#     stack.append(i)
def dfs():
    for i in range(0, 10):
        if len(stack) == 0 or stack[-1] > i:
            stack.append(i)
            num = int("".join(list(map(str, stack))))
            result.append(num)
            dfs()
            stack.pop()

dfs()
result.sort()
try:
    print(result[N - 1])    
except:
    print(-1)


