arr = list(map(int, input().split(" ")))
arr.sort()

if arr[0] + arr[1] > arr[2]:
    print(sum(arr))
else:
    two_sum = arr[0] + arr[1]
    print(two_sum * 2 - 1)
