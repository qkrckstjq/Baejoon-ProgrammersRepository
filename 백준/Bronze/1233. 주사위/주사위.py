a, b, c = map(int, input().split(" "))
counter = {i : 0 for i in range(3, a + b + c + 1)}
max_target = float('inf')
max_num = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            sum = i + j + k
            counter[sum] += 1
            if (counter[sum] > max_num) or (counter[sum] == max_num and sum < max_target):
                max_target = sum
                max_num = counter[sum]

print(max_target)
