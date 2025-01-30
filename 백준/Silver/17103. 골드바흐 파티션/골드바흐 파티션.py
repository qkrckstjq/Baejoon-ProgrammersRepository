T = int(input())
def get_prime(num):
    prime = [True] * (num + 1)
    for i in range(2, int(num*0.5) + 1):
        if prime[i]:
            for j in range(i**2, num, i):
                prime[j] = False
    prime_list = [i for i in range(2, len(prime)) if prime[i]]
    return set(prime_list), prime_list

prime_set, prime_list = get_prime(1000000)

for _ in range(T):
    N = int(input())
    used = set()
    i = 0
    result = 0
    while prime_list[i] < N:
        # if prime_list[i] in used:
        #     i += 1
        #     continue
        if prime_list[i] not in used and (N - prime_list[i]) in prime_set:
            result += 1
            used.add(prime_list[i])
            used.add(N - prime_list[i])
        i += 1
    print(result)