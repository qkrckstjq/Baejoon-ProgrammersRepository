import sys

def s_input():
    return sys.stdin.readline().strip()

result = []
while True:
    str_input = input()
    if str_input == '.':
        break
    stack = []

    for w in str_input:
        if w == '(' or w == '[':
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(w)
                break


    if not stack:
        result.append("yes")
    else:
        result.append("no")


for r in result:
    print(r)