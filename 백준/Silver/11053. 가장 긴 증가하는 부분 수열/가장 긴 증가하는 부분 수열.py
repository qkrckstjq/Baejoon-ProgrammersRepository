import bisect
lis = []
N = int(input())
arr = list(map(int, input().split(" ")))
for num in arr:
    pos = bisect.bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num

result = len(lis)
print(result)