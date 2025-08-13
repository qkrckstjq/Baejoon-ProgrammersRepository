m = {"R" : [0, 1], 
        "L" : [0,-1],
        "B" : [-1,0],
        "T" : [1, 0],
        "RT" : [1,1],
        "LT" : [1,-1],
        "RB" : [-1,1],
        "LB" : [-1,-1]}

x = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7}
w = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H"}

king, rock, n = list(input().split(" "))

king = [int(king[1]) - 1, x[king[0]]]
rock = [int(rock[1]) - 1, x[rock[0]]]

move = [input() for _ in range(int(n))]
for q in move:
    dy, dx = m[q]
    n_y = king[0] + dy
    n_x = king[1] + dx
    if (0 <= n_y < 8) and (0 <= n_x < 8):
        if (n_y == rock[0]) and (n_x == rock[1]):
            r_y = rock[0] + dy
            r_x = rock[1] + dx
            if (0 <= r_y < 8) and (0 <= r_x < 8):
                rock = [r_y, r_x]
                king = [n_y, n_x]
        else:
            king = [n_y, n_x]

print(w[king[1]]+str(king[0] + 1) + '\n' + w[rock[1]]+str(rock[0] + 1))
            