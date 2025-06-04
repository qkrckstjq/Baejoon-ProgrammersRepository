answer = []
for i in range(3):
    result = 0
    num = int(input())
    for j in range(num):
        result += int(input())
        
    if result == 0:
        answer.append("0")
    elif result > 0:
        answer.append("+")
    else:
        answer.append("-")

for r in answer:
    print(r)