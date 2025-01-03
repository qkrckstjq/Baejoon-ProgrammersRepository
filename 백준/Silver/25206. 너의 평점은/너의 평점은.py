total = 0
total_score = 0
num = 0

score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
}

while True:
    try:
        a, b, c = input().split(" ")
        if c == "P":
            continue
        else:
            total += float(score[c]) * float(b)
            total_score += float(b)
    except:
        break
print(round(total / total_score, 6))