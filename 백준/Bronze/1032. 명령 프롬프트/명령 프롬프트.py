T = int(input())
input_list = list()
for i in range(T):
    input_list.append(list(input()))
        

answer = list()

for i in range(len(input_list[0])):
    for j in range(len(input_list)):
        if len(answer) <= i:
            answer.append(input_list[j][i])
        else:
            if answer[i] == input_list[j][i]:
                continue
            elif answer[i] != input_list[j][i]:
                answer[i] = "?"
                
print("".join(answer))