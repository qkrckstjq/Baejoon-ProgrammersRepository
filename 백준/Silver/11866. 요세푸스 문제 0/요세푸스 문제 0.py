from collections import deque
N, K = map(int, input().split(" "))
arr = deque([i for i in range(1, N + 1)])
answer = []
while arr:
    for _ in range(K - 1):
        arr.append(arr.popleft())
    answer.append(arr.popleft())

    
result = ", ".join(list(map(str, answer)))
print(f"<{result}>")
