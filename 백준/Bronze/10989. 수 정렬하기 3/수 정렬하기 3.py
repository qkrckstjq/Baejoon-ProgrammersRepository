N = int(input())
arr = [0 for _ in range(10001)]

for _ in range(N):
    arr[int(input())] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)