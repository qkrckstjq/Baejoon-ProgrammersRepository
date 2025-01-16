N = int(input())

def sum_num(n):
    n_arr = list(str(n))
    result = n
    for num in n_arr:
        result += int(num)
    return result

find = False
for num in range(1, 1000000):
    if sum_num(num) == N:
        print(num)
        find = True
        break
if not find:
    print(0)
