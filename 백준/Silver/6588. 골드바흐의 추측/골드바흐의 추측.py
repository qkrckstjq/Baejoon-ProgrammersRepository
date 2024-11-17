import copy
big_prime = 2
prime_list = []

def get_prime_list(n):
    prime = [True for _ in range(n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i**2, n + 1, i):
                prime[j] = False
    return [num for num in range(2, len(prime)) if prime[num]]

while True:
    prime = int(input())
    if prime == 0:
        break
    prime_list.append(prime)
    big_prime = max(big_prime, prime)

prime = get_prime_list(big_prime)
set_prime = set(copy.copy(prime))

for num in prime_list:
    b = 0
    a = 0
    for i in prime:
        a = i
        if (num - a) in set_prime:
            b = num - a
            break
    print(f"{num} = {a} + {b}")