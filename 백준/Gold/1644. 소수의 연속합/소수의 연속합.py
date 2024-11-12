N = int(input())

def get_prime(a):
    prime = [True for _ in range(a + 1)]
    for i in range(2, int(a**0.5) + 1):
        if prime[i]:
            for j in range(i**2, a + 1, i):
                prime[j] = False
    return [num for num in range(2, a + 1) if prime[num]]

prime = get_prime(N)
count = 0

for i in range(len(prime)):
    number = 0
    for j in range(i, len(prime)):
        number += prime[j]
        if N == number:
            count += 1
            break
        if number > N:
            break
        

print(count)