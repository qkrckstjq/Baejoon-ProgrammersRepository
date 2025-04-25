N = int(input())
memo = [-1] * (N + 1)
memo[0] = 0
memo[1] = 1

def fibo(N):
    if N <= 1:
        return N
    if memo[N] != -1:
        return memo[N]
    
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

print(fibo(N))