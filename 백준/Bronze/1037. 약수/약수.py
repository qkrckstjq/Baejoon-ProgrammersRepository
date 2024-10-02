count = int(input())
divisors = list(map(int, input().split()))
N = min(divisors) * max(divisors)
print(N)