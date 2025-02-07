N = int(input())
numbers = list(map(int, input().split(" ")))
answer = [0, float('inf')]
numbers.sort()

di = [0, 0, 1, 0]
dj = [0, -1, 1, -1]

i = 0
j = len(numbers) - 1
# print(numbers)
while i < j:
    sum_num = numbers[i] + numbers[j]
    first = numbers[i]
    second = numbers[j]
    sum_ans = answer[0] + answer[1]
    
    if abs(sum_num) < abs(sum_ans):
        answer = [first, second]
    
    if answer[0] + answer[1] == 0:
        break
        
    if sum_num < 0:
        i += 1
    elif sum_num > 0:
        j -= 1
    

print(f"{answer[0]} {answer[1]}")