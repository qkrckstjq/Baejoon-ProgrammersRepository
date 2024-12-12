def solution(park, routes):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    direct = {"E" : 2, "S" : 0, "W" : 3, "N" : 1}
    grid = [list(i) for i in park]
    def check_range(y, x):
        return True if 0 <= y < len(grid) and 0 <= x < len(grid[0]) else False
    cur_y, cur_x = 0, 0
    find = False
    for i in range(len(grid)):
        if find:
            break
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                cur_y, cur_x = i, j
                find = True
                break
    
    for command in routes:
        d, cnt = command.split(" ")
        cnt = int(cnt)
        next_y, next_x = cur_y, cur_x
        for i in range(cnt):
            next_y += dy[direct[d]]
            next_x += dx[direct[d]]
            if check_range(next_y, next_x) and grid[next_y][next_x] != "X":
                if i == cnt - 1:
                    cur_y = next_y
                    cur_x = next_x
            else:
                break
        
    answer = [cur_y, cur_x]
    return answer