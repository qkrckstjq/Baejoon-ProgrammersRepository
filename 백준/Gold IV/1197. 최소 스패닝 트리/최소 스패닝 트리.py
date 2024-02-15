import sys
input = sys.stdin.readline

def find_parent(parent, x):
    """ 부모 노드를 찾기 위해 재귀 수행"""
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    """ 부모 노드 비교 후 부모 노드 업데이트 """
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
if __name__ == "__main__":
    V, E = map(int, input().split()) # make graph
    graph = [] 
    for _ in range(E):
        a, b, cost = map(int, input().split())
        graph.append([a, b, cost])
    graph.sort(key=lambda x:x[2])

    parent = [0] * (V+1) # make parent table
    for i in range(1, V+1):
        parent[i] = i

    costs, mst = 0, [] # get mst
    for i in range(E):
        a, b, cost = graph[i]
        if find_parent(parent, a) != find_parent(parent, b): # check cycle
            union_parent(parent, a, b)
            mst.append((a, b))
            costs += cost

    print (costs)