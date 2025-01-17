T = int(input())
arr = [1, 1, 1, 2, 2, 3]

def get(num):
    if num <= len(arr):
        return arr[num - 1]
    last = arr[-1]
    second = arr[(len(arr) - 1) - 4]
    arr.append(last + second)
    return get(num)

for _ in range(T):
    num = int(input())
    print(get(num))