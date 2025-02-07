N, M, start = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)

# 인접 리스트 정렬 (오름차순)
for i in range(1, N + 1):
    graph[i].sort()

cnt = 1
answer = [0] * (N + 1)
visit = [False] * (N + 1)

stack = [start]

while stack:
    cur_node = stack.pop()
    
    if not visit[cur_node]:  # 방문하지 않은 경우만 처리
        visit[cur_node] = True
        answer[cur_node] = cnt
        cnt += 1
        
        # 인접 노드를 역순으로 추가 (스택 특성상 역순으로 처리)
        for next_node in reversed(graph[cur_node]):
            if not visit[next_node]:
                stack.append(next_node)

# 출력
for i in range(1, N + 1):
    print(answer[i])
