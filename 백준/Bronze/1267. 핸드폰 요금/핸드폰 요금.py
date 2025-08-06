n = int(input())
time_list = map(int, input().split(" "))

Y = 0
M = 0
for t in time_list:
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if Y < M:
    print(f"Y {Y}")
elif Y > M:
    print(f"M {M}")
else:
    print(f"Y M {Y}")
    
