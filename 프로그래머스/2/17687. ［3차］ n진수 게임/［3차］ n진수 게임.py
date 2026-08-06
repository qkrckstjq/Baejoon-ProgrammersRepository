def solution(n, t, m, p):
    answer = ''
    string = ''
    num = 0
    while len(string) < t * m:
        string += trans(num, n)
        num += 1
    
    # print(string)
    for i in range(0, t * m, m):
        answer += string[i + (p - 1)]
    
    return answer

def trans(num, n):
    result = []
    a = 1
    b = 1
    while a != 0:
        a = num // n
        b = num % n
        num = a
        if b >= 10:
            result.append(chr(b + 55))
            continue
        result.append(str(b))
    result.reverse()
    return "".join(result)