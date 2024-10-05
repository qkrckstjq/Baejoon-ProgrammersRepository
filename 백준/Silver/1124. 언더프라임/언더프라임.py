def find_prime(num, primes):
    for prime in primes:
        if num % prime == 0:
            return num // prime
    return 1

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def count_steps_and_check_prime(target, primes, sieve):
    count = 0
    while target != 1:
        target = find_prime(target, primes)
        count += 1
    return sieve[count]  # count가 소수인지 확인

# 입력받기
A, B = map(int, input().split())

# 범위 B에 맞춰서 소수 리스트를 생성
primes = sieve_of_eratosthenes(B)
sieve = [False] * (B + 1)
for prime in primes:
    sieve[prime] = True

answer = 0
for target in range(A, B + 1):
    if count_steps_and_check_prime(target, primes, sieve):
        answer += 1

print(answer)
