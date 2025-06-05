m = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
while(True):
    result = 0
    sentens = input()
    if(sentens == '#'):
        break
    for w in sentens:
        if(w in m):
            result += 1
    print(result)
    