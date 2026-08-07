def solution(n, q, ans):
    answer = 0
    arr = comb(n, len(q[0]))
    for t in arr:
        temp = set(t)
        is_pass = True
        for i, c in enumerate(q):
            cnt = 0
            for num in c:
                if num in temp:
                    cnt += 1
                if cnt > ans[i]:
                    break
            if cnt != ans[i]:
                is_pass = False
        if is_pass:
            answer += 1
        
    return answer

def comb(num, r):
    result = []
    temp = []
    
    
    def dfs(t):
        if len(temp) == r:
            result.append(temp[:])
            return
        
        for i in range(t, num + 1):
            temp.append(i)
            dfs(i + 1)
            temp.pop()
    dfs(1)
    
    return result
        