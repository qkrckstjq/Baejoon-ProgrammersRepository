N, B = map(int, input().split(" "))
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

def time_matrix(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (a[i][k] * b[k][j])
            result[i][j] %= 1000
    return result

def process(mat, b):
    if b == 1:
        return [[x % 1000 for x in row] for row in mat]
    half = process(mat, b // 2)
    if b % 2 == 0:
        return time_matrix(half, half)
    else:
        return time_matrix(mat, time_matrix(half, half))
      
result = process(matrix, B)

for i in range(N):
    row = ""
    for j in range(N):
        row += str(result[i][j]) + " "
    print(row)