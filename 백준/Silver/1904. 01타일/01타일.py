N = int(input())
if N <= 3:
    print(N)
else:
    prev_1 = 1
    prev_2 = 2
    answer = 3
    for i in range(3, N + 1):
        answer = (prev_1 + prev_2) % 15746
        prev_1 = prev_2
        prev_2 = answer
    print(answer)