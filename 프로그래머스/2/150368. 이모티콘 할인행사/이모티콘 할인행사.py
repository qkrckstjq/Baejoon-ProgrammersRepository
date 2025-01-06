def solution(users, emoticons):
    emo = { e : 0 for e in emoticons}    
    
    def proccess():
        result = [0, 0]
        # print(emo)
        for per, money in users:
            total_pay = 0
            for pay, e_per in emo.items():
                if per <= e_per:
                    total_pay += (pay - ((pay * e_per) // 100))
                    if total_pay >= money:
                        result[0] += 1
                        total_pay = 0
                        break
            result[1] += total_pay
        # print(result)
        return result
                        
    def dfs(index, answer):
        if index == len(emoticons):
            answer.append(proccess())
            return
        for per in [10, 20, 30, 40]:
            emo[emoticons[index]] = per
            dfs(index + 1, answer)
    answer = []    
    dfs(0, answer)
    answer.sort(key=lambda x:(x[0], x[1]), reverse=True)
    # print(answer)
    return answer[0]