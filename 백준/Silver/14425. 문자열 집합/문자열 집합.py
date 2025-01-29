N, M = map(int, input().split(" "))
hash_map = set()
[hash_map.add(input()) for _ in range(N)]
answer = 0
for _ in range(M):
    word = input()
    if word in hash_map:
        answer += 1
print(answer)