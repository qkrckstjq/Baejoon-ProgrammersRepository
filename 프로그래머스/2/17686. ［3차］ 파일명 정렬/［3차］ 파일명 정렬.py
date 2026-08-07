def solution(files):
    answer = []
    # print(ord('1'))
    # print(getHead("F-5 Freedom Fighter"))
    # print(getNumber("F-5 Freedom Fighter"))
    files.sort(key = lambda x : (getHead(x), getNumber(x)))
    return files

def getHead(string):
    result = ''
    for i in range(len(string)):
        c = ord(string[i])
        if 48 <= c <= 57:
            break
        result += string[i]
    return result.upper()

def getNumber(string):
    result = ''
    idx = 0
    for i in range(idx, len(string)):
        if 48 <= ord(string[i]) <= 57:
            idx = i
            break
    
    for i in range(idx, len(string)):
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            break
            
        result += string[i]
    
    return int(result)
    
        
    