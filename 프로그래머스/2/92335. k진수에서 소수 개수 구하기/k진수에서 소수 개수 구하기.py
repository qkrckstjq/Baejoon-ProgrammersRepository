import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def solution(n, k):
    arr = []

    while n:
        arr.append(str(n % k))
        n //= k

    converted = ''.join(arr[::-1])

    answer = 0

    for num in converted.split('0'):
        if num == '':
            continue

        if is_prime(int(num)):
            answer += 1

    return answer