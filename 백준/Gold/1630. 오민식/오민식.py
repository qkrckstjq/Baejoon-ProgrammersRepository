import math
N = int(input())

def uclid(a, b):
    big = 0
    small = 0
    if a > b:
        big = a
        small = b
    elif a < b:
        big = b
        small = a
    else:
        return a
    
    if big % small == 0:
        return small
    else:
        return uclid(small, big % small)

def find_prime(N):
    prime = [True for _ in range(N + 1)]
    for i in range(2, int(N**0.5) + 1):
        if prime[i**2]:
            for j in range(i**2, N + 1, i):
                prime[j] = False
    return math.prod([max_prime(i, N) for i in range(2, N + 1) if prime[i]]) % 987654321

def max_prime(num, N):
    times = num
    while num <= N:
        num *= times
    return num // times
    
result = find_prime(N)

print(result)