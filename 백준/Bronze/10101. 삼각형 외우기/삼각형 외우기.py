A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180:
    if A == 60 and B == 60 and C == 60:
        print("Equilateral")
    elif A == B or A == C or B == C:
        print("Isosceles")
    elif A != B != C:
        print("Scalene")
else:
    print("Error")