matrix_y = {}
matrix_x = {}
for _ in range(3):
    y, x = map(int, input().split(" "))
    if y in matrix_y:
        matrix_y[y] += 1
    else:
        matrix_y[y] = 1
    if x in matrix_x:
        matrix_x[x] += 1
    else:
        matrix_x[x] = 1
answer = ""
for y in matrix_y.keys():
    if matrix_y[y] == 1:
        answer += f"{y} "
for x in matrix_x.keys():
    if matrix_x[x] == 1:
        answer += f"{x}"
print(answer)