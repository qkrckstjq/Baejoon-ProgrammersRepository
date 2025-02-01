N = int(input())

answer = 0
visit = set()
for _ in range(N):
    word = input()
    if word == "ENTER":
        visit = set()
        continue
    
    if not word in visit:
        answer += 1
        visit.add(word)
    

print(answer)