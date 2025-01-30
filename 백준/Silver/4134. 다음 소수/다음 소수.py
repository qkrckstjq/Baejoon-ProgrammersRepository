T = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(T):
    num = int(input())
    while not is_prime(num):
        num += 1
    print(num)