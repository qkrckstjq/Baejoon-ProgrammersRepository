def solution(ingredient):
    rec = [1, 3, 2, 1]
    def make_hamburger(arr):
        if len(arr) < 4:
            return False
        last_idx = len(arr) - 1
        idx = 0
        for i in range(last_idx, last_idx - 4, -1):
            if arr[i] != rec[idx]:
                return False
            idx += 1
        for _ in range(4):
            arr.pop()
            
        return True
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if make_hamburger(stack):
            
            answer += 1
    
    return answer