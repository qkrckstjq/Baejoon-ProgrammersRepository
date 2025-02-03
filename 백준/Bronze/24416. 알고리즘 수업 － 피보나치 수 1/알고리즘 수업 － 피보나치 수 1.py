N = int(input())

answer_a = 0
answer_b = 0
def fibo(num):
    global answer_a
    if num <= 2:
        answer_a += 1
        return 1
    return fibo(num - 1) + fibo(num - 2)

memo = [False] * 41
def fibo_memo(num):
    global answer_b
    if num <= 2:
        answer_b += 1
        return 1
    if memo[num]:
        answer_b += 1
        return memo[num]
    memo[num] = fibo_memo(num - 1) + fibo_memo(num - 2)
    return memo[num]

fibo(N)
fibo_memo(N)
print(answer_a, answer_b - 1)