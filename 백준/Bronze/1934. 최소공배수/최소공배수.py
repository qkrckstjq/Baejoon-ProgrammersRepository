N = int(input())

def uclid(a, b):
    cur_a = a
    cur_b = b
    while a % b != 0:
        a, b = b, a % b
    return (cur_a * cur_b // b)

for _ in range(N):
    a, b = map(int, input().split(" "))
    print(uclid(a, b))