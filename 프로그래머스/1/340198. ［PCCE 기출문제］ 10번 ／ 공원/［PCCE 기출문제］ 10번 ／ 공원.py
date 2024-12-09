def solution(mats, park):
    mats.sort(reverse=True)
    dy = [1, 0]
    dx = [0, 1]
    def dfs(size, y, x):
        if len(park) - y < size or len(park[0]) - x < size:
            return False
        stack = [(y, x, 1, 1)]
        visit = set()
        while stack:
            cur_y, cur_x, p_y, p_x = stack.pop()
            if park[cur_y][cur_x] != "-1":
                return False
            for i in range(2):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                next_py = p_y + dy[i]
                next_px = p_x + dx[i]
                if (next_y, next_x) not in visit and next_py <= size and next_px <= size:
                    stack.append((next_y, next_x, next_py, next_px))
                    visit.add((next_y, next_x))
        return True
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if dfs(mat, i, j):
                    return mat

    return -1