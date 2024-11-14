from collections import deque

T = int(input())

for _ in range(T):
    # 입력 처리
    N, K = map(int, input().split())
    delay = list(map(int, input().split()))
    
    # 그래프와 진입 차수 배열 초기화
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    
    # 간선 정보 입력 처리
    for _ in range(K):
        require, dst = map(int, input().split())
        graph[require].append(dst)
        indegree[dst] += 1
    
    target = int(input())

    # 각 노드까지 걸리는 최대 시간을 저장할 배열
    time = [0] * (N + 1)

    # 진입 차수가 0인 노드를 큐에 삽입하고 초기 시간 설정
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            time[i] = delay[i - 1]
    
    # 위상 정렬 시작
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            # 최대 시간 갱신 (선행 노드 시간 + 현재 노드의 건설 시간)
            time[next_node] = max(time[next_node], time[node] + delay[next_node - 1])
            indegree[next_node] -= 1
            
            # 진입 차수가 0이 되면 큐에 삽입
            if indegree[next_node] == 0:
                queue.append(next_node)

    # 목표 노드까지 걸리는 최대 시간 출력
    print(time[target])