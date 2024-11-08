min_x, max_x = map(int, input().split(" "))
total_num = max_x - min_x + 1
is_used = [False] * total_num

for i in range(2, int(max_x**0.5) + 1):
    number = i**2
    start = ((min_x + number - 1) // number) * number
    
    for j in range(start, max_x + 1, number):
        if min_x <= j <= max_x and not is_used[j - min_x]:
            is_used[j - min_x] = True
            total_num -= 1

print(total_num)
