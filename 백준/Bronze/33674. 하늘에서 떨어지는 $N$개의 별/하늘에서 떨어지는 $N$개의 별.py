N, D, K = map(int, input().split(" "))
s_list = list(map(int, input().split(" ")))
stars = [0] * len(s_list)
answer = 0

for _ in range(D):
    clean = False
    
    for i in range(len(s_list)):
        if stars[i] + s_list[i] > K:
            clean = True
            break
    
    if clean:
        stars = [0] * len(s_list)
        answer += 1
    
    for i in range(len(s_list)):
        stars[i] += s_list[i]

print(answer)