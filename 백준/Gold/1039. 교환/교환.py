import copy
N, M = list(input().split(" "))
N = list(N)
M = int(M)

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


stack = [(N, 0)]
answer = -1
visit = {i : set() for i in range(1, M + 1)}
while stack:
    cur_n, cur_k = stack.pop()
    if cur_k == M:
        answer = max(answer, int("".join(cur_n)))
        continue
    for i in range(len(cur_n)):
        for j in range(i + 1, len(cur_n)):
            if not (i == 0 and cur_n[j] == "0"):
                copy_n = copy.deepcopy(cur_n) 
                swap(i, j, copy_n)
                next_n = "".join(copy_n)
                if not next_n in visit[cur_k + 1]:
                    visit[cur_k + 1].add(next_n)
                    stack.append((copy_n, cur_k + 1))

print(answer)