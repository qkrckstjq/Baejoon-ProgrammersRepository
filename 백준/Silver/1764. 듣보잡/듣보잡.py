N, M = map(int, input().split(" "))
diagram = set()
answer = []

for _ in range(N):
    diagram.add(input())

for _ in range(M):
    input_value = input()
    if input_value in diagram:
        answer.append(input_value)

answer.sort()
print(len(answer))
[print(value) for value in answer]