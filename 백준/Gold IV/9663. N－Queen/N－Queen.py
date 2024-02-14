queen = int(input())
result = 0
arr = [-1] * queen

def is_Impossible(s, x):
    for i in range(s, x, 1):
        if arr[i] == arr[x] or x - i == abs(arr[i] - arr[x]):
            return True
    return False

stack = []
for i in range(queen - 1, -1, -1):
    stack.append([i, 0])

while stack:
    cur_y, cur_x = stack.pop()
    arr[cur_x] = cur_y

    if cur_x == queen - 1:
        result += 1
        continue
    else:
        for i in range(queen):
            arr[cur_x + 1] = i
            if not is_Impossible(0, cur_x + 1):
                stack.append([i, cur_x + 1])




print(result)