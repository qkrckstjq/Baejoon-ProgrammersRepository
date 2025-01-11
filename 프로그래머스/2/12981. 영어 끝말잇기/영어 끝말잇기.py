def solution(n, words):
    answer = [0, 0]
    
    cnt = 0
    prev = None
    used = set()
    for word in words:
        cnt += 1
        if (prev != None and prev[-1] != word[0]) or word in used:
            return [cnt - (cnt // n - (1 if cnt % n == 0 else 0)) * n, cnt // n + (0 if cnt % n == 0 else 1)]
        prev = word
        used.add(word)
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer