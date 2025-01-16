A, B = map(int, input().split(" "))
def fact(num):
    if num == 0:
        return 1
    if num <= 2:
        return num
    return num * fact(num - 1)
print(int(fact(A) / (fact(A - B) * fact(B))))