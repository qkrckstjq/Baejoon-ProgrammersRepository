import sys
from collections import deque
def sInput():
    return sys.stdin.readline().strip()

T = int(sInput())

for i in range(T):
    input_words = sInput()
    password = deque()
    shifted_word = deque()

    for c in input_words:
        if c == '<':
            if len(password) != 0:
                shifted_word.appendleft(password.pop())
            continue
        if c == '-':
            if len(password) != 0:
                password.pop()
            continue
        if c == '>':
            if len(shifted_word) != 0:
                password.append(shifted_word.popleft())
            continue

        password.append(c)

    while len(shifted_word) != 0:
        password.append(shifted_word.popleft())

    print("".join(password))