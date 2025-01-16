N = int(input())
string = list(input())

answer = 0

for i in range(len(string)):
    answer += ((31**i) * (ord(string[i]) - 96))

print(answer)