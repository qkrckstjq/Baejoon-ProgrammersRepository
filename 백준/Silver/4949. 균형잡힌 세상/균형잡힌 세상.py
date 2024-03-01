import sys

def s_input():
    return sys.stdin.readline().strip()

result = []
while True:
    str_input = input()
    if str_input == '.':
        break
    stack = []

    for c in str_input:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif c == ']' or c == ')':
            stack.append(c)
            break

    if len(stack) == 0:
        result.append("yes")
    else:
        result.append("no")


for r in result:
    print(r)