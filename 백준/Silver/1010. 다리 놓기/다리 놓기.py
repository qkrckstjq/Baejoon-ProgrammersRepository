import sys

memo = []

def s_input():
    return sys.stdin.readline().strip()

def facto(num):
    if num <= 1:
        return 1
    elif num <= len(memo):
        return memo[num]
    else:
        return num * facto(num - 1)

def combination(n, r):
    return facto(n) // (facto(n - r) * facto(r))

T = int(s_input())

for i in range(T):
    i, j = list(map(int, s_input().split(" ")))
    n = max(i, j)
    r = min(i, j)
    print(combination(n, r))