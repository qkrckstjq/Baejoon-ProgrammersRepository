t = int(input())

for i in range(t):
    stack = 0
    s = input()
    for c in s:
        stack += 1 if c == '(' else -1
        if stack < 0:
            print("NO")
            break

    if stack == 0:
        print("YES")
    if stack > 0:
        print("NO")

