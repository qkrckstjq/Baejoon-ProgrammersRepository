words = input()
hash_map = set()
for i in range(len(words)):
    cur_w = ""
    for j in range(i, len(words)):
        cur_w += words[j]
        hash_map.add(cur_w)
            
# print(hash_map)
print(len(hash_map))

