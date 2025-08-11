N = int(input())

triangle = []
for i in range(N):
    row = [list(map(int, input().split(" "))), [0 for _ in range(i + 1)]]
    triangle.append(row)

# print(triangle)
triangle[0][1][0] = triangle[0][0][0]
for i in range(N - 1):
    for j in range(len(triangle[i][0])):
        cur_v = triangle[i][1][j]
        if (cur_v + triangle[i + 1][0][j]) > triangle[i + 1][1][j]:
            triangle[i + 1][1][j] = (cur_v + triangle[i + 1][0][j])
        if (cur_v + triangle[i + 1][0][j + 1]) > triangle[i + 1][1][j + 1]:
            triangle[i + 1][1][j + 1] = (cur_v + triangle[i + 1][0][j + 1])

print(max(triangle[-1][1]))