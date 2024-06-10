# from collections import defaultdict

def solution(genres, plays):
    answer = []
    total = {}
    seperate = {}
    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
            seperate[genres[i]].append(i)
        else:
            total[genres[i]] = plays[i]
            seperate[genres[i]] = [i]
    total_list = []
    
    for key, value in total.items():
        total_list.append({key : value})
    total_list = sorted(total_list, key=lambda x: list(x.values())[0], reverse=True)
    
    print(total_list)
    
    for i in range(len(total_list)):
        best_g = list(total_list[i].keys())[0]
        best_i = sorted(seperate[best_g], key = lambda x:plays[x], reverse=True)
        if len(best_i) >= 2:
            answer.append(best_i[0])
            answer.append(best_i[1])
        else:
            answer.append(best_i[0])
    
    return answer