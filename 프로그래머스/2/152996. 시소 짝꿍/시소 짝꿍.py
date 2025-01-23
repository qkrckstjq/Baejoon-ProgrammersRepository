def solution(weights):
    answer = 0
    unique = {}
    
    for w in weights:
        if w in unique:
            unique[w] += 1
        else:
            unique[w] = 1

    for w, count in unique.items():
        if count > 1:
            answer += count * (count - 1) // 2
    
    def check_match(a, b):
        for i in range(2, 5):
            cur_a = a * i
            for j in range(2, 5):
                cur_b = b * j
                if cur_a == cur_b:
                    return True
        return False
    unique_keys = list(unique.keys())
    for i in range(len(unique_keys) - 1):
        for j in range(i + 1, len(unique_keys)):
            if check_match(unique_keys[i], unique_keys[j]):
                answer += (unique[unique_keys[i]] * unique[unique_keys[j]])
            
    return answer