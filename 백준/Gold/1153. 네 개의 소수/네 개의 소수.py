N = int(input())

def get_prime_list(number):
    prime = [True for _ in range(number + 1)]
    prime[0], prime[1] = False, False
    for i in range(2, int(number**0.5) + 1):
        if prime[i]:
            for j in range(i**2, number + 1, i):
                prime[j] = False
    return [i for i in range(2, len(prime)) if prime[i]]

def result(prime_list, target):
    for n1 in prime_list:
        for n2 in prime_list:
            for n3 in prime_list:
                n4 = target - n1 - n2 - n3
                if n4 in prime_list:
                    return [n1, n2, n3, n4]
    return -1

prime_list = get_prime_list(N)
prime = set(prime_list)
answer = result(prime, N)

if answer == -1:
    print(-1)
else:
    print(" ".join(list(map(str, answer))))
