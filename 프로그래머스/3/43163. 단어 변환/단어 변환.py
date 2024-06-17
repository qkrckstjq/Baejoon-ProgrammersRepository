from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    visited.add(begin)
    
    while queue:
        cur_word, cnt = queue.popleft()
        
        if cur_word == target:
            return cnt
        
        for i in range(len(cur_word)):
            for j in range(97, 123):  # ASCII 'a' to 'z'
                next_word = cur_word[:i] + chr(j) + cur_word[i+1:]
                
                if next_word in words and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, cnt + 1))
    
    return 0
