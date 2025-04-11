X, Y, D, T = map(int, input().split(" "))

dist = (X**2 + Y**2) ** 0.5
jump = dist // D

case1 = dist

if dist >= D:
    case2 = jump * T + (dist - jump * D)
    case3 = (jump + 1) * T
    print(min(case1, min(case2, case3)))
else:
    case2 = T + (D - dist)
    case3 = T * 2
    print(min(case1, min(case2, case3)))