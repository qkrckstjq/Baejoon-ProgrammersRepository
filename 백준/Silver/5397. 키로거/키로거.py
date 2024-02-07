import sys
from collections import deque
def sInput():
    return sys.stdin.readline().strip()

T = int(sInput())

for i in range(T):
    key_log = sInput()
    password = deque()
    temp_key = deque()

    for c in key_log:
        if c == '<':
            if len(password) != 0:
                temp_key.appendleft(password.pop())
            continue
        if c == '-':
            if len(password) != 0:
                password.pop()
            continue
        if c == '>':
            if len(temp_key) != 0:
                password.append(temp_key.popleft())
            continue

        password.append(c)

    while len(temp_key) != 0:
        password.append(temp_key.popleft())

    print("".join(password))