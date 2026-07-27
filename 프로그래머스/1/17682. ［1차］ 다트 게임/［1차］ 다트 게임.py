def solution(dartResult):
    answer = 0
    stack = []
    p = {"S" : 1, "D" : 2, "T" : 3}
    for i in range(len(dartResult)):
        d = dartResult[i]
        if i > 0 and dartResult[i - 1] == "1" and d == "0":
            continue
        if d in p:
            last = stack.pop()
            stack.append(last**p[d])
        elif d == "*":
            for i in range(len(stack) - 1, max(-1, len(stack) - 3), -1):
                stack[i] = stack[i] * 2
        elif d == "#":
            stack[-1] = stack[-1] * -1
        else:
            if d == "1" and dartResult[i + 1] == "0":
                stack.append(10)
            else:
                stack.append(int(d))
            
    return sum(stack)