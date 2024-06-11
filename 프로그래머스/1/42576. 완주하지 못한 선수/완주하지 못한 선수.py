def solution(participant, completion):
    count_p = {}
    for player in participant:
        if player in count_p:
            count_p[player] += 1
        else:
            count_p[player] = 1
    
    for player in completion:
        if player in count_p:
            count_p[player] -= 1
            if count_p[player] == 0:
                del count_p[player]
    
    answer = list(count_p.keys())[0]
    
    return answer