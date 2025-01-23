N = int(input())
prev_max = [0, 0, 0]
max_num = [0, 0, 0]

min_num = [0, 0, 0]
prev_min = [0, 0, 0]

def get_value(x, max_cur, min_cur):
    if x == 0:
        return [max([max_cur + prev_max[0], max_cur + prev_max[1]]), min([min_cur + prev_min[0], min_cur + prev_min[1]])]
    elif x == 1:
        return [max([max_cur + prev_max[0], max_cur + prev_max[1], max_cur + prev_max[2]]), min([min_cur + prev_min[0], min_cur + prev_min[1], min_cur + prev_min[2]])]
    else:
        return [max([max_cur + prev_max[1], max_cur + prev_max[2]]), min([min_cur + prev_min[1], min_cur + prev_min[2]])] 

for i in range(N):
    row = list(map(int, input().split(" ")))
    if i > 0:
        max_num = [num for num in row]
        min_num = [num for num in row]
        for j in range(3):
            max_num[j], min_num[j] = get_value(j, max_num[j], min_num[j])
        prev_max = [num for num in max_num]
        prev_min = [num for num in min_num]
    else:
        prev_max = [num for num in row]
        prev_min = [num for num in row]
        
        max_num = [num for num in row]
        min_num = [num for num in row]
    

print(max(max_num), min(min_num))