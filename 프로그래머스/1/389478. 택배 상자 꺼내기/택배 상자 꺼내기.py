def solution(n, w, num):
    answer = 0
    for i in range(1, w + 1):
        y1 = (w * 2) - 1 - ((i - 1) * 2)
        y2 = 1 + ((i - 1) * 2)
        c = True
        while True:
            if i >= num:
                break
                
            i += (y1 if c else y2)
            c = not c
            
        if i == num:
            
            answer = 1
            while True:
                i += (y1 if c else y2)
                c = not c    
                if i > n:
                    break
                else:
                    answer += 1

    return answer