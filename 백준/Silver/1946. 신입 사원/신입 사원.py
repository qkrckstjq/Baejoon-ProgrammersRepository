import sys

def s_input():
    return sys.stdin.readline().strip()

T = int(s_input())
for i in range(T):
    num = int(s_input())
    document_list = []
    for j in range(num):
        a, b = list(map(int, s_input().split(" ")))
        document_list.append((a, b))
    document_list.sort(key=lambda x:x[0])
    base_a, base_b = document_list[0]
    result = 1
    for i in range(1, len(document_list)):
        if document_list[i][0] < base_a or document_list[i][1] < base_b:
            base_a = document_list[i][0]
            base_b = document_list[i][1]
            result += 1
    print(result)