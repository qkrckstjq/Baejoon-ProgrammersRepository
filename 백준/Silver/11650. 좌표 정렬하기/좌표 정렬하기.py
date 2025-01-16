N = int(input())
arr = []
for _ in range(N):
    y, x = map(int, input().split(" "))
    arr.append((y, x))
arr.sort(key=lambda x:(x[0], x[1]))
[print(y, x) for y, x in arr]