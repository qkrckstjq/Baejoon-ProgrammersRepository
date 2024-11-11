A, B = list(map(int, input().split(" ")))

def get_sqrt_prime(B):
    limit = int(B**0.5) + 1
    prime = [True for _ in range(limit)]
    for i in range(2, limit):
        if prime[i]:
            for j in range(i**2, limit, i):
                prime[j] = False
    return prime

def get_result(prime_list, A, B):
    result = 0
    for i in range(2, len(prime_list)):
        if prime_list[i]:
            power_num = i**2
            while power_num <= B:
                if A <= power_num <= B:
                    result += 1
                power_num *= i
    return result

prime = get_sqrt_prime(B)
print(get_result(prime, A, B))