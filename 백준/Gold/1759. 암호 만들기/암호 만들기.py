import sys

# Get Inputs
L, C = list(map(int, sys.stdin.readline().split(" ")))
chars = sys.stdin.readline().split()
chars.sort()


def contains(cur_string: str) -> bool:
    set_chars = set(chars)
    set_cur_string = set(cur_string)

    vowels = {'a', 'e', 'i', 'o', 'u'}
    in_consonant = set_chars - vowels
    in_vowel = set_chars - in_consonant

    cur_consonant = set_cur_string - in_vowel
    cur_vowel = set_cur_string - cur_consonant

    return len(cur_consonant) > 1 and cur_vowel



def subsets(strs: list):
    rst = []

    def dfs(start, visited: str):
        if len(visited) == L and contains(visited) and visited not in rst:
            rst.append(visited)
            return

        for i in range(start, len(strs)):
            dfs(i + 1, visited + strs[start])

    for i in range(C):
        dfs(i, "")
    return rst


for str in subsets(chars):
    print(str)