N = int(input())
stack = []
answer = []
for _ in range(N):
    input_list = list(map(int, input().split(" ")))
    command = 0
    num = 0
    if len(input_list) == 2:
        command = input_list[0]
        num = input_list[1]
    else:
        command = input_list[0]
    if command == 1:
        stack.append(num)
    elif command == 2:
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif command == 3:
        answer.append(len(stack))
    elif command == 4:
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    elif command == 5:
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
[print(a) for a in answer]