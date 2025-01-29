N = int(input())
hash_map = set(list(map(int, input().split(" "))))
answer = []
M = int(input())
target_list = list(map(int, input().split(" ")))
for num in target_list:
    if num in hash_map:
        answer.append("1")
    else:
        answer.append("0")
print(" ".join(answer))    