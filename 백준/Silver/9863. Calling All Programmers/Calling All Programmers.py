import sys
from collections import deque

def s_input():
    return sys.stdin.readline()

result = []

while True:
    n, m, k = list(map(int, s_input().split(" ")))
    queue = deque()
    if n == 0 and m == 0 and k == 0:
        break

    for i in range(1, n + 1, 1):
        queue.append(i)

    winner = 0
    for _ in range(k):
        for i in range(m):
            popped = queue.popleft()
            if i == m - 1:
                winner = popped
                # print("뽑힌 공 : " + str(winner))
            else:
                queue.append(popped)
            # print(queue)
    result.append(winner)

for a in result:
    print(a)