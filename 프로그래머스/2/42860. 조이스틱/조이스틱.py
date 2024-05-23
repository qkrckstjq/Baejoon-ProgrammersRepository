def solution(name):
    a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8,
         'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    answer = 0
    move = len(name) - 1
    
    for i in range(len(name)):
        answer += a[name[i]]  # 위아래 이동 횟수 계산
        
        # 다음 문자가 'A'인 경우 다음으로 이동할 문자를 찾음
        next_non_a_idx = i + 1
        while next_non_a_idx < len(name) and name[next_non_a_idx] == 'A':
            next_non_a_idx += 1
        
        # 좌우 이동 거리 계산
        move = min(move, i + len(name) - next_non_a_idx + min(i, len(name) - next_non_a_idx))
    
    return answer + move