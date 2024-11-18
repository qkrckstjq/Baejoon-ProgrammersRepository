from collections import deque

N = int(input())
if N == 1:
    print(0)
else:
    def append_queue(queue, n, cnt):
        if n % 3 == 0:
            queue.append((n // 3, cnt + 1))
        if n % 2 == 0:
            queue.append((n // 2, cnt + 1))
        queue.append((n - 1, cnt + 1))

    queue = deque()
    append_queue(queue, N, 0)
    used = set()
    while queue:
        cur_n, cur_cnt = queue.popleft()
        if cur_n in used:
            continue
        if cur_n == 1:
            print(cur_cnt)
            break
        used.add(cur_n)
        append_queue(queue, cur_n, cur_cnt)
