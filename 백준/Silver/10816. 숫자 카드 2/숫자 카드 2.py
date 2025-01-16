N = int(input())
n_input = list(input().split(" "))
n_dict = {}
for num in n_input:
    if num in n_dict:
        n_dict[num] += 1
    else:
        n_dict[num] = 1
M = int(input())
m_input = list(input().split(" "))
answer = []
for key in m_input:
    if key in n_dict:
        answer.append(n_dict[key])
    else:
        answer.append(0)
[print(i) for i in answer]

