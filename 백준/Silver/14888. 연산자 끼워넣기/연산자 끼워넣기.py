N = int(input())
numbers = list(map(int, input().split(" ")))
math = list(map(int, input().split(" ")))

def eval(a, b, i):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    elif i == 3:
        if a < 0:
            return -((-a) // b)
        return a // b

max_sum = -float('inf')
min_sum = float('inf')
def dfs(prev, i):
    global numbers, max_sum, min_sum
    if i == len(numbers):
        max_sum = max(max_sum, prev)
        min_sum = min(min_sum, prev)
    
    for j in range(4):
        if math[j] > 0:
            math[j] -= 1
            dfs(eval(prev, numbers[i], j), i + 1)
            math[j] += 1

dfs(numbers[0], 1)

print(max_sum)
print(min_sum)