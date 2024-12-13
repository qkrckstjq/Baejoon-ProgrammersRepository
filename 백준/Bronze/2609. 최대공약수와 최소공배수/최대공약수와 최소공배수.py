A, B = map(int, input().split(" "))

def uclid(A, B):
    while A % B != 0:
        A, B = B, A % B
    return B

result = uclid(A, B)
print(result)
print(A * B // result)
