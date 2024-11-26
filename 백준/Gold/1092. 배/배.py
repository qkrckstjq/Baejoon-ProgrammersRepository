N = int(input())
crains = list(map(int, input().split(" ")))
crains.sort(reverse=True)
M = int(input())
boxes = list(map(int, input().split(" ")))
boxes.sort()

if boxes[-1] > crains[0]:
    print(-1)
else:
    result = 0
    while boxes:
        find = False
        for crain in crains:
            for j in range(len(boxes) - 1, -1, -1):
                box = boxes[j]
                if crain >= box:
                    find = True
                    boxes.pop(j)
                    break
        result += 1
    print(result)
