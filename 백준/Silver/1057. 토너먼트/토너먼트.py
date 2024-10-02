def get_next(a):
    if a % 2 == 0:
        return a // 2
    else:
        return (a + 1) // 2

round, N, M = list(map(int, input().split(" ")))

answer = 1
while get_next(N) != get_next(M):
    N = get_next(N)
    M = get_next(M)
    answer += 1
    
print(answer)