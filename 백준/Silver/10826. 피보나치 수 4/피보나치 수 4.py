N = int(input())
memo = [0, 1]

if N <= 1:
    print(memo[N])
else:
    for _ in range(N - 1):
        a = memo[0]
        b = memo[1]
        memo[0] = b
        memo[1] = a + b
    print(memo[1])