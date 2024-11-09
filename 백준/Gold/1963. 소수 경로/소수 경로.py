from collections import deque
import copy

T = int(input())

def get_prime_list():
    prime = [True for _ in range(10000)]
    prime[0], prime[1] = False, False
    for i in range(2, int(10000**0.5) + 1):
        if prime[i]:
            for j in range(i**2, 10000, i):
                prime[j] = False
    return set([i for i in range(2, 10000) if prime[i]])

def bfs(start, target, prime):
    queue = deque()
    used = set()
    queue.append((start, 0))
    used.add(start)
    while queue:
        cur_num, count = queue.popleft()
        if cur_num == target:
            return count
        split = list(map(int, str(cur_num)))
        for i in range(4):
            for j in range(0, 10):
                copy_split = copy.deepcopy(split)
                copy_split[i] = j
                next_num = int("".join(list(map(str, copy_split))))
                if 1000 <= next_num <= 9999 and (next_num not in used) and (next_num in prime):
                    queue.append((next_num, count + 1))
                    used.add(next_num)
    return "Impossible"

        
        
prime = get_prime_list()
for _ in range(T):
    a, b = list(map(int, input().split(" ")))
    print(bfs(a, b, prime))

# print("".join(list(map(str, [1,5,4,6]))))