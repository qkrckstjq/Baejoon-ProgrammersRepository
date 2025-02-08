N = int(input())
numbers = list(map(int, input().split(" ")))
target = int(input())

numbers.sort()

i = 0
j = len(numbers) - 1
answer = 0
while i < j:
    sum_num = numbers[i] + numbers[j]
    if sum_num < target:
        i += 1
    elif sum_num > target:
        j -= 1
    else:
        answer += 1
        i += 1
        j -= 1

print(answer)