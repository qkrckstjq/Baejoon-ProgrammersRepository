def solution(k, dungeons):
    answer = 0

    def dfs(health, dungeons, visited, count):
        nonlocal answer
        if count > answer:
            answer = count

        for i in range(len(dungeons)):
            if not visited[i] and health >= dungeons[i][0]:
                visited[i] = True
                dfs(health - dungeons[i][1], dungeons, visited, count + 1)
                visited[i] = False

    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)

    return answer