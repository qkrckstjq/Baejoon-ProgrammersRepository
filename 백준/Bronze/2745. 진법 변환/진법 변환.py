words, N = input().split(" ")
N = int(N)
answer = 0

for i in range(len(words)):
    num = 0
    if 'A' <= words[i] <= 'Z':
        num = ord(words[i]) - 55
    else:
        num = int(words[i])
    # print((N ** (len(words) - i - 1)))
    answer += (N ** (len(words) - i - 1)) * num

print(answer)