import sys

def s_input():
    return sys.stdin.readline().strip()

def dfs(string):
    stack = [(string, '')]
    combinations = []

    while stack:
        current, path = stack.pop()

        if len(current) == 0:
            combinations.append(path)
            continue

        for i in range(len(current)):
            next_string = current[:i] + current[i+1:]
            stack.append((next_string, path + current[i]))
    combinations.reverse()
    return combinations

N = int(s_input())
for i in range(N):
    string = list(s_input())
    result = dfs(string)
    case = "Case # "+str(i + 1)+":"
    print(case)
    for s in result:
        print(s)


