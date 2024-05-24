p1 = [1, 2, 3, 4, 5]
p2 = [2, 1, 2, 3, 2, 4, 2, 5]
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    a1, i = 0, 0
    a2, j = 0, 0
    a3, k = 0, 0
    
    def check_idx(index, arr):
        if index + 1 < len(arr):
            return index + 1
        else:
            return 0
    
    for item in answers:
        if p1[i] == item:
            a1 += 1
        if p2[j] == item:
            a2 += 1
        if p3[k] == item:
            a3 += 1
        i = check_idx(i, p1)
        j = check_idx(j, p2)
        k = check_idx(k, p3)
    
    max_score = max(a1, a2, a3)
    
    top_students = []
    if a1 == max_score:
        top_students.append(1)
    if a2 == max_score:
        top_students.append(2)
    if a3 == max_score:
        top_students.append(3)
    
    return top_students
            
            