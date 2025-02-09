N = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort()
answer = [0, float('inf'), 0]
for i in range(N - 2):
    j = i + 1
    k = N - 1
    if answer[0] + answer[1] + answer[2] == 0:
        break
    while j < k:
        sum_num = numbers[i] + numbers[j] + numbers[k]
        sum_ans = answer[0] + answer[1] + answer[2]
        if abs(sum_num) < abs(sum_ans):
            answer = [numbers[i], numbers[j], numbers[k]]
            
        if sum_num < 0:
            j += 1
        else:
            k -= 1

print(" ".join(list(map(str, answer))))