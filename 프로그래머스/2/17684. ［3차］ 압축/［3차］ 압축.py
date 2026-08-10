def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):
        dic[chr(i + 64)] = i
    
    # print(dic)
    
    i = 0
    while i < len(msg):
        s = msg[i]
        while True:
            i += 1
            if i >= len(msg):
                break
            if s + msg[i] not in dic:
                dic[s + msg[i]] = len(dic) + 1
                break
            s += msg[i]
        answer.append(dic[s])

    # print(dic)
    return answer