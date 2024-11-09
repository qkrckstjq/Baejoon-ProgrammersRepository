import sys
import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def find_four_primes_sum(N):
    primes = sieve(N)
    prime_set = set(primes)

    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                p4 = N - p1 - p2 - p3
                if p4 in prime_set:
                    return p1, p2, p3, p4
    return -1

N = int(input())
result = find_four_primes_sum(N)

if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))
