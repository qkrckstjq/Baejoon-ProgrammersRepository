T = int(input())

def fact(num):
    if num == 0:
        return 1
    if num <= 2:
        return num
    return num * fact(num - 1)

for _ in range(T):
    N = int(input())
    dict = {}
    result = 1
    for _ in range(N):
        A, B = input().split(" ")
        if B in dict:
            dict[B].append(A)
        else:
            dict[B] = [A]
    
    for key in dict.keys():
        result *= (len(dict[key]) + 1)
    
    result -= 1
    print(result)