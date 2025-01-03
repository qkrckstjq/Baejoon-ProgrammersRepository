grid = []
max_x = 0
while True:
    try:
        words = list(input())
        max_x = max(max_x, len(words))
        grid.append(words)
    except:
        break

answer = ""
for i in range(max_x):
    for j in range(len(grid)):
        if i > len(grid[j]) - 1:
            continue
        else:
            answer += grid[j][i]
print(answer)