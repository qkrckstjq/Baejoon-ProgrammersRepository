word = input()

i, j = 0, 0
if len(word) % 2 == 0:
    i = len(word) // 2 - 1
    j = len(word) // 2
else:
    i = len(word) // 2 - 1
    j = len(word) // 2 + 1

pal = True
for n in range(len(word) // 2):
    if word[i - n] != word[j + n]:
        print(0)
        pal = False
        break

if pal:
    print(1)
