from collections import deque

def solution(order):
    src = deque()
    for i in range(1, len(order) + 1):
        src.append(i);
    sub = []
    answer = 0
    for num in order:
        suc = False;
        while True:
            if len(src) > 0 and src[0] == num:
                suc = True
                src.popleft()
                break
            elif len(sub) > 0 and sub[-1] == num:
                suc = True
                # print(src)
                # print(sub)
                # print("\n")
                sub.pop()
                break
            else:
                if(len(src) == 0):
                    break
                sub.append(src.popleft())
        if suc:
            answer += 1
        else:
            break
                       
    return answer