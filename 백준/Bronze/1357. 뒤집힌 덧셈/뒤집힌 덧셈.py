a, b = input().split(" ")

def rev(num):
    temp = []
    for i in range(len(num) - 1, -1, -1):
        if i != len(num):
            temp.append(num[i])
        elif num[i] != "0":
            temp.append(num[i])
            
    return int("".join(temp))

print(rev(str(rev(a) + rev(b))))
