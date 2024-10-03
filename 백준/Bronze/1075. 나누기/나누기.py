N = list(input())
F = int(input())

N[len(N) - 1] = '0'
N[len(N) - 2] = '0'
N = int("".join(N))
if N % F == 0:
    result = list(str(N))
    answer = result[-2] + result[-1]
    print(answer)
else:
    result = list(str((N // F) * F + F))
    answer = result[-2] + result[-1]
    print(answer)