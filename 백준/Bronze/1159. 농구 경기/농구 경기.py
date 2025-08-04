N = int(input())
name_list = []
[name_list.append(input()) for _ in range(N)]
count = {}

for i in range(N):
    first_word = name_list[i][0]
    if first_word in count:
        count[first_word] += 1
    else:
        count[first_word] = 1

result = []
for key, value in count.items():
    if value >= 5:
        result.append(key)
        
if len(result) == 0:
    print("PREDAJA")
else:
    result.sort()
    print("".join(result))