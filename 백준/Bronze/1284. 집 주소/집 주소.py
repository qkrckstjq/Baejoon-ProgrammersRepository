while True:
    n = input()
    if n == '0':
        break
    result = len(n) + 1
    for num in n:
        num = int(num)
        if num == 1:
            result += 2
        elif num == 2:
            result += 3
        elif num == 0:
            result += 4
        else:
            result += 3
    print(result)