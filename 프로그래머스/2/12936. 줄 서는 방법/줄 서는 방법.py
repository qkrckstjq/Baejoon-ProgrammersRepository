def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))

    k -= 1

    factorial = 1
    for i in range(1, n):
        factorial *= i

    for i in range(n, 0, -1):
        index = k // factorial

        answer.append(numbers.pop(index))

        k %= factorial

        if i > 1:
            factorial //= (i - 1)

    return answer