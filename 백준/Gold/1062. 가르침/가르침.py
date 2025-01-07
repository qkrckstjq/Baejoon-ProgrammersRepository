N, K = map(int, input().split(" "))
words = []

for _ in range(N):
    word = list(input())
    words.append(set(word))

char = set(list("antatica"))
alphabet = [chr(i) for i in range(97, 123) if chr(i) not in char]
comb = K - len(char)

def check_word(base_words):
    global words
    result = 0
    for word in words:
        pos = True
        for c in word:    
            if not c in base_words:
                pos = False
                break
        result += (1 if pos else 0)
    return result

answer = 0
def dfs(index):
    global comb, answer
    if len(char) - 5 == comb:
        answer = max(answer, check_word(char))
        return True
    
    for i in range(index, len(alphabet)):
        char.add(alphabet[i])
        dfs(i + 1)
        char.remove(alphabet[i])
        
            

if comb < 0:
    print(0)
else:
    dfs(0)
    print(answer)