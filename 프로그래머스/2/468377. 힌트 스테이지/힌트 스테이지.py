stage = []
answer = 12345678910

def solution(cost, hint):
    global answer
    global stage
    
    hint_dict = {i : 0 for i in range(1, len(cost) + 1)}
    stage = cost
    dfs(1, hint, hint_dict, 0)
    
    return answer

def dfs(i, hint, hint_state, cur_cost):
    global stage
    global answer
    if i > len(hint) + 1:
        answer = min(answer, cur_cost)
    else:
        new_hint_state = hint_state.copy()
        not_buy_hint_cost = cur_cost + stage[i - 1][new_hint_state[i]]
        dfs(i + 1, hint, new_hint_state, not_buy_hint_cost)
        
        if i < len(hint) + 1:
            for idx in range(1, len(hint[i - 1])):
                new_hint_state[hint[i - 1][idx]] += 1
                if new_hint_state[hint[i - 1][idx]] > len(hint):
                    new_hint_state[hint[i - 1][idx]] = len(hint)
            # print("기존 %d, 힌트 구매 비용 %d, 스테이지 클리어 %d\n", cur_cost, hint[i - 1][0], stage[i - 1][new_hint_state[i]])
            buy_hint_cost = cur_cost + (stage[i - 1][new_hint_state[i]] + hint[i - 1][0])
            dfs(i + 1, hint, new_hint_state, buy_hint_cost)
        