A_1, B_1 = map(int, input().split(" "))
A_2, B_2 = map(int, input().split(" "))

def uclid(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

result_b = B_1 * B_2 // uclid(B_1, B_2)
result_a = (A_1 * (result_b // B_1)) + (A_2 * (result_b // B_2))

temp = uclid(result_a, result_b)
print(result_a // temp, result_b // temp)