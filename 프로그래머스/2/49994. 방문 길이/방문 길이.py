def solution(dirs):
    answer = 0
    visit = {}
    cur_y = 0
    cur_x = 0
    for d in dirs: 
        next_y = cur_y
        next_x = cur_x
        if d == "U":
            next_y = min(5, cur_y + 1)
        elif d == "D":
            next_y = max(-5, cur_y - 1)
        elif d == "L":
            next_x = max(-5, cur_x - 1)
        elif d == "R":
            next_x = min(5, cur_x + 1)
        if cur_y == next_y and cur_x == next_x:
            continue
        if not (cur_y, cur_x) in visit or not (next_y, next_x) in visit[(cur_y, cur_x)]:
            answer += 1
            if (cur_y, cur_x) in visit:
                visit[(cur_y, cur_x)].add((next_y, next_x))
            else:
                visit[(cur_y, cur_x)] = set([(next_y, next_x)])
            
            if (next_y, next_x) in visit:
                visit[(next_y, next_x)].add((cur_y, cur_x))
            else:
                visit[(next_y, next_x)] = set([(cur_y, cur_x)])
            
        cur_y = next_y
        cur_x = next_x
    # print(visit)
    return answer

