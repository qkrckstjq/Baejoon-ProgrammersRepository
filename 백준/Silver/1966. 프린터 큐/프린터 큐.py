import heapq

T = int(input())

for i in range(T):
    NM = list(map(int, input().split(" ")))
    Nodes = NM[0]
    targetNode = NM[1]
    indexValue = list(enumerate(map(int, input().split(" "))))
    maxPQ = []
    for i in range(len(indexValue)):
        heapq.heappush(maxPQ, -indexValue[i][1])

    count = 1
    front = 0
    peek = -heapq.heappop(maxPQ)
    while True:
        while indexValue[front][1] != peek:
            pushBack = indexValue[front]
            indexValue.append(pushBack)
            front += 1

        if indexValue[front][0] == targetNode:
            print(count)
            break

        if indexValue[front][1] == peek:
            count += 1
            front += 1
            peek = -heapq.heappop(maxPQ)
            continue