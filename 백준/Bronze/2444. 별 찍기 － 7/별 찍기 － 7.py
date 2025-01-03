N = int(input())

for i in range(N):
    word = ""
    for _ in range((N - i) - 1):
        word += " "
    for _ in range(2):
        for _ in range(i):
            word += "*"
    word += "*"
    print(word)
    
for i in range(N - 1):
    word = ""
    for _ in range(i + 1):
        word += " "
    for _ in range(2):
        for _ in range((N - i) - 2):
            word += "*"
    word += "*"
    print(word)