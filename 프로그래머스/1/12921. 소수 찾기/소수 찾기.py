def solution(n):
    prime = [True for _ in range(n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if prime[i * i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return len([i for i in range(2, len(prime)) if prime[i]])