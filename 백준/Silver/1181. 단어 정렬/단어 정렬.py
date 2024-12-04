N = int(input())
words = []
words_set = set()
for _ in range(N):
    word = input()
    if word in words_set:
        continue
    words.append(word)
    words_set.add(word)

words.sort(key=lambda x: (len(x), x))
[print(word) for word in words]