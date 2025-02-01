N = int(input())
graph = set(["ChongChong"])
for _ in range(N):
    src, dst = list(input().split(" "))
    if src in graph or dst in graph:
        graph.add(src)
        graph.add(dst)
print(len(graph))