N = int(input())
peoples = list(map(int, input().split(" ")))
T, P = map(int, input().split(" "))
result1 = 0
for num in peoples:
    result1 += (num // T) + (1 if num % T != 0 else 0)
    # elif num % T == 0:
    #     result1 += (num // T)
    # else:
    #     result1 += (num // T) + 1

print(result1)
print(N // P, N % P)
