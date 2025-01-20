from collections import deque
def solution(s):
    def check(s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack
    
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.append(s.popleft())
        if check(s):
            answer += 1
    return answer