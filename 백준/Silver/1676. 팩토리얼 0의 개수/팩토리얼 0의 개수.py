N = int(input())

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num - 1)
zero = 0
answer = fact(N)
num_list = list(str(answer))
for i in range(len(num_list) - 1, -1, -1):
    if num_list[i] == "0":
        zero += 1
    else:
        break

print(zero)