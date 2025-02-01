N = int(input())

count = 0
def recursion(word, i, j):
    global count
    count += 1
    if i >= j:
        return True
    if word[i] != word[j]:
        return False
    return recursion(word, i + 1, j - 1)

for _ in range(N):
    count = 0
    word = input()
    print(1 if recursion(word, 0, len(word) - 1) else 0, count)