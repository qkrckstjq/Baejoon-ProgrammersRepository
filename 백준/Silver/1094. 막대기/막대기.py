X = int(input())
stick = 64

def proccess(target):
    answer = 1
    total = 64
    prev = 64
    min_stick = 64
    while total != target:
        min_stick //= 2
        answer += 1
        if total - min_stick >= target:
            total -= min_stick
            answer -= 1
    print(answer)

proccess(X)
    
    
