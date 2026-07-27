is_ill = True
def solution(new_id):
    new_id = new_id.lower()
    print(new_id)
    new_id = remove_str(new_id)
    print(new_id)
    
    
#     new_id = remove_dup_dot(new_id)
#     print(new_id)
    
#     new_id = remove_lf_dot(new_id)
#     print(new_id)
    
#     new_id = fill_a(new_id)
#     print(new_id)
    
#     new_id = over_16(new_id)
#     print(new_id)
    
#     new_id = fill_las(new_id)
#     print(new_id)
    
    
    global is_ill
    while is_ill:
        is_ill = False
        new_id = remove_dup_dot(new_id)
        new_id = remove_lf_dot(new_id)
        new_id = fill_a(new_id)
        new_id = over_16(new_id)
        new_id = fill_las(new_id)
    
    return new_id

def remove_str(new_id):
    result = ""
    for i in range(len(new_id)):
        s = new_id[i]
        if s.isdecimal() or 97 <= ord(s) <= 122:
            result += s
        elif s == "-" or s == "_" or s == ".":
            result += s
    return result

def remove_dup_dot(new_id):
    global is_ill
    result = ""
    for i in range(len(new_id)):
        if len(result) > 0 and result[-1] == "." and new_id[i] == ".":
            is_ill = True
            continue
        result += new_id[i]
    return result

def remove_lf_dot(new_id):
    global is_ill
    start = len(new_id)
    end = 0
    
    for i in range(0, len(new_id)):
        if new_id[i] != ".":
            start = i
            break
    
    for i in range(len(new_id) - 1, -1, -1):
        if new_id[i] != ".":
            end = i
            break
            
    # print(start, end)        
    if start > end:
        is_ill = True
        return ""
    
    if start != 0 or end != len(new_id) - 1:
        is_ill = True
    
    return new_id[start : end + 1]

def fill_a(new_id):
    global is_ill
    if len(new_id) == 0:
        return "aaa"
    return new_id

def over_16(new_id):
    global is_ill
    if len(new_id) >= 16:
        is_ill = True
        return new_id[0 : 15]
    return new_id

def fill_las(new_id):
    global is_ill
    dif = 3 - len(new_id)
    if len(new_id) <= 2:
        is_ill = True
        return new_id + new_id[-1] * dif
    
    return new_id