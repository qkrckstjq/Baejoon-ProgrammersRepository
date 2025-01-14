while True:
    A, B, C = map(int, input().split(" "))
    if A == B == C == 0:
        break
    arr = [A, B, C]
    arr.sort()
    if arr[0] + arr[1] <= arr[2]:
        print("Invalid")
    elif A == B == C:
        print("Equilateral")
    elif A == B or B == C or A == C:
        print("Isosceles")
    elif A != B != C:
        print("Scalene")