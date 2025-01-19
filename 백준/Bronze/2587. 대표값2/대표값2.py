arr = []
while True:
    try:
        num = int(input())
        arr.append(num)
    except:
        break

arr.sort()

avg = sum(arr) // len(arr)
if len(arr) % 2 == 0:
    mid = int((arr[len(arr) // 2] + arr[len(arr) // 2 -  1]) // 2)
else:
    mid = arr[len(arr) // 2]

print(avg)
print(mid)
