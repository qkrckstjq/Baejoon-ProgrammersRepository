X, Y, D, T = map(int, input().split(" "))

dist = (X**2 + Y**2)**0.5

# jump = dist 방향으로 점프할 수 있는 최대 경우
jump = dist//D

if dist >= D:
    case1 = T * jump + (dist - (D * jump))
    case2 = dist
    case3 = T * (jump + 1)
    
    result = min(case1, min(case2, case3))
    result = round(result,9)
    print(result)

else:
    case1 = T + (D - dist)
    case2 = dist
    case3 = T * 2
    
    result = min(case1, min(case2, case3))
    result = round(result,9)
    print(result)