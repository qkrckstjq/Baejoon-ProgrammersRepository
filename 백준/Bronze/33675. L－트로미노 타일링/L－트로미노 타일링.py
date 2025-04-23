T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print(2 ** (N // 2))
    else:
        print(0)