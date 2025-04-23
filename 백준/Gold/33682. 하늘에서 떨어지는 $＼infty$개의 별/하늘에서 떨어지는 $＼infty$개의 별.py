import sys

s0, X, M, D, K = map(int, input().split())

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

g = gcd(X, M)
r = s0 % g
max_s = M - g + r

# 별이 전혀 쌓이지 않으면 0을 출력하고 바로 종료
if max_s == 0:
    print(0)
    sys.exit()

R = K // max_s
cleans = (D - 1) // R
print(cleans)