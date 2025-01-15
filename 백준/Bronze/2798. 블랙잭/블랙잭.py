N, target = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
answer = -float('inf')

for i in range(len(arr)):
    num_i = arr[i]
    if num_i > target:
        continue
    for j in range(i + 1, len(arr)):
        num_j = num_i + arr[j]
        if num_j > target:
            continue
        for k in range(j + 1, len(arr)):
            num_k = num_j + arr[k]
            if num_k > target:
                continue
            if target - num_k < target - answer:
                answer = num_k
print(answer)