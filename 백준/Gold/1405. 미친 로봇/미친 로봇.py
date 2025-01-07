K, E, W, N, S = map(int, input().split(" "))

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

move = [E, W, N, S]

answer = 0
visit = set()

def dfs(cur, cnt, per):
    global answer
    if cur in visit:
        return
    
    if cnt == K:
        answer += per
        return
    
    visit.add(cur)
    cur_y, cur_x = cur
    for i in range(4):
        if move[i] > 0:
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            dfs((next_y, next_x), cnt + 1, per * (move[i] / 100))
    visit.remove(cur)
            
dfs((0, 0), 0, 1)

print(answer)