N = int(input())
hash_map = set()
for _ in range(N):
    name, op = input().split()
    if op == "enter":
        hash_map.add(name)
    else:
        hash_map.remove(name)

hash_map = sorted(list(hash_map), reverse=True)
[print(name) for name in hash_map]