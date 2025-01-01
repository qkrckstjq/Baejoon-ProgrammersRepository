def solution(wallpaper):
    min_y, min_x, max_y, max_x = float('inf'), float('inf'), 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(list(wallpaper[0]))):
            if wallpaper[i][j] == "#":
                min_y = min(min_y, i)
                min_x = min(min_x, j)
                max_y = max(max_y, i)
                max_x = max(max_x, j)
                
    
    answer = [min_y, min_x, max_y + 1, max_x + 1]
    
    return answer