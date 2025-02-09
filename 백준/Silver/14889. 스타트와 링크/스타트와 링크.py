N = int(input())
grid = []
for _ in range(N):
    row = list(map(int, input().split(" ")))
    grid.append(row)

start = []
link = []

def cal(team):
    global grid
    result = 0
    for i in range(len(team) - 1):
        for j in range(i + 1, len(team)):
            result += (grid[team[i]][team[j]] + grid[team[j]][team[i]])
    return result
answer = float('inf')
def dfs(start, last):
    global answer
    if len(start) * 2 == N:
        link = [i for i in range(N) if i not in start]
        start_score = cal(start)
        link_score = cal(link)
        # print(start, link, start_score, link_score)
        answer = min(answer, abs(start_score - link_score))
        return
    
    for i in range(last + 1, N):
        start.append(i)
        dfs(start, i)
        start.pop()

dfs([], -1)

print(answer)