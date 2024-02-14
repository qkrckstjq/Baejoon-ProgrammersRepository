import sys

def s_input():
    return sys.stdin.readline()

num = int(s_input())

stack = []
stack2 = []
result = []

for i in range(num, 0, -1):
    stack.append(i)

while stack or stack2:
    key, repeat = list(map(int, (s_input().split(" "))))
    if key == 1:
        for _ in range(repeat):
            stack2.append(stack.pop())
    elif key == 2:
        for _ in range(repeat):
            result.append(stack2.pop())

for i in range(len(result) - 1, -1, -1):
    print(result[i])