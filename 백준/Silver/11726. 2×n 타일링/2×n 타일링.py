N = int(input())
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibo(idx):
    if len(arr) > idx:
        return arr[idx]
    last = arr[-1]
    second = arr[len(arr) - 2]
    arr.append(last + second)
    return fibo(idx)

print(fibo(N) % 10007)