def solution(arr):
    zero = 0
    one = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                zero += 1
            elif arr[i][j] == 1:
                one += 1
                
    def press(y1, x1, y2, x2, zero, one):
        # print(y1, x1, y2, x2)
        if (y2 - y1) == 1 or (x2 - x1) == 1:
            return zero, one
        prev = arr[y1][x1]
        for y in range(y1, y2):
            for x in range(x1, x2):
                if arr[y][x] != prev:
                    z1, o1 = press(y1, x1, (y1 + y2) // 2, (x1 + x2) // 2, zero, one)
                    z2, o2 = press((y1 + y2) // 2, x1, y2, (x1 + x2) // 2, z1, o1)
                    z3, o3 = press(y1, (x1 + x2) // 2, (y1 + y2) // 2, x2, z2, o2)
                    return press((y1 + y2) // 2, (x1 + x2) // 2, y2, x2, z3, o3)
        pressed = (x2 - x1) * (y2 - y1)
        if prev == 0:
            zero -= (pressed - 1)
        else:
            one -= (pressed - 1)
        return zero, one
            
    zero, one = press(0, 0, len(arr), len(arr[0]), zero, one)
    return [zero, one]