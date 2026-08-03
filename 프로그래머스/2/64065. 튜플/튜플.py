def solution(s):
    answer = []
    dup = set()
    sorted_list = [list(map(int, x.split(","))) for x in s[2:-2].split("},{")] 
    sorted_list.sort(key = lambda x: len(x))
    # print(sorted_list)
    for t in sorted_list:
        for num in t:
            if not num in dup:
                answer.append(num)
                dup.add(num)
    
    return answer