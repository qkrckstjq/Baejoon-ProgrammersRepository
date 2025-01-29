a, b = map(int, input().split(" "))

def uclid(a, b):
    cur_a = a
    cur_b = b
    while a % b != 0:
        a, b = b, a % b
    return cur_a * cur_b // b

print(uclid(a, b))