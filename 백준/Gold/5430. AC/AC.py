from collections import deque
T = int(input())
def input_filter(str):
    result = []
    if len(str) == 2:
        return result
    word = ''
    for i in range(1, len(str)):
        if str[i] == ',' or str[i] == ']':
            result.append(int(word))
            word = ''
            continue
        else:
            word += str[i]
    return result
            

for _ in range(T):
    command = list(input())
    list_num = int(input())
    numbers = deque(input_filter(input()))
    revers = False
    is_error = False
    for c in command:
        if c == 'R':
            revers = not revers
        elif c != 'R' and len(numbers) <= 0:
            is_error = True
            break
        elif c == 'D' and revers:
            numbers.pop()
        else:
            numbers.popleft()
    if is_error:
        print('error')
    else:
        if revers:
            numbers.reverse()
        print('[' + ','.join(map(str, numbers)) + ']')