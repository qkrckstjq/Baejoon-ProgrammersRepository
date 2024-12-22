dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def solution(land):
    def check_range(y, x):
        return True if 0 <= y < len(land) and 0 <= x < len(land[0]) else False
    
    index = 0
    def find_oil(y, x, visit, total_visit):
        nonlocal index
        if (y, x) in total_visit:
            now_index = total_visit[(y, x)]["0"]
            if now_index in visit:
                return 0
            else:
                visit.add(now_index)
                return total_visit[(y, x)]["1"]  
        index += 1
        visit.add((y, x))
        stack = [(y, x)]
        result = 1
        route = [(y, x)]
        while stack:
            cur_y, cur_x = stack.pop()
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if check_range(next_y, next_x):
                    if land[next_y][next_x] == 1 and (next_y, next_x) not in visit:
                        result += 1
                        stack.append((next_y, next_x))
                        visit.add((next_y, next_x))
                        route.append((next_y, next_x))
        
        for y, x in route:
            total_visit[(y, x)] = {}
            total_visit[(y, x)]["0"] = index
            total_visit[(y, x)]["1"] = result
        visit.add(index)
        return result

    answer = 0
    total_visit = {}
    
    for i in range(len(land[0])):
        visit = set()
        oil = 0
        for j in range(len(land)):
            if land[j][i] == 1:
                oil += find_oil(j, i, visit, total_visit)
        # print(oil)
        answer = max(oil, answer)
    return answer