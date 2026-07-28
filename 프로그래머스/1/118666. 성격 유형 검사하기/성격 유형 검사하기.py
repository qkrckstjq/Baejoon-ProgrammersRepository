score = {"R" : 0, "T" : 0,
            "C" : 0, "F" : 0,
            "J" : 0, "M" : 0,
            "A" : 0, "N" : 0
            }
def solution(survey, choices):
    answer = ''
    no1 = {"R" : 0, "T" : 0}
    no2 = {"C" : 0, "F" : 0}
    no3 = {"J" : 0, "M" : 0}
    no4 = {"A" : 0, "N" : 0}
    
    global score
    
    for i in range(len(survey)):
        t = survey[i]
        c = choices[i]
        
        point = abs(4 - c)
        
        if c > 4:
            score[t[1]] += point
        elif c < 4:
            score[t[0]] += point
            
    
    answer += (getH("R", "T") + getH("C", "F") + getH("J", "M") + getH("A", "N"))
    
        
    return answer

def getH(a, b):
    global score
    first = score[a]
    second = score[b]
    if first >= second:
        return a
    else:
        return b
    