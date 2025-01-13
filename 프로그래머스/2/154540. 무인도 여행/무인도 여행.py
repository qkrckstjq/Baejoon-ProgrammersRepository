visit = set()
def solution(maps):
    answer = []
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    def dfs(y, x):
        global visit
        visit.add((y, x))
        result = int(maps[y][x])
        stack = [[y, x]]
        while stack:
            cur_y, cur_x = stack.pop()
            
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if 0 <= next_y < len(maps) and 0 <= next_x < len(maps[0]) and (next_y, next_x) not in visit and maps[next_y][next_x] != "X":
                    result += int(maps[next_y][next_x])
                    stack.append([next_y, next_x])
                    visit.add((next_y, next_x))
        return result
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != "X" and (y, x) not in visit:
                answer.append(dfs(y, x))
        answer.sort()
    return answer if len(answer) != 0 else [-1]