grid = {
    1 : (0, 0),
    2 : (0, 1),
    3 : (0, 2),
    4 : (1, 0),
    5 : (1, 1),
    6 : (1, 2),
    7 : (2, 0),
    8 : (2, 1),
    9 : (2, 2),
    "*" : (3, 0),
    0 : (3, 1),
    "#" : (3, 2)
}

left = set([1, 4, 7, "*"])
right = set([3, 6, 9, "#"])

def solution(numbers, hand):
    answer = ''
    cur_left = (3, 0)
    cur_right = (3, 2)
    
    
    def get_dis(y, x, y1, x1):
        return abs(y - y1) + abs(x - x1)
    
    for num in numbers:
        if num in left:
            answer += "L"
            cur_left = grid[num]            
        elif num in right:
            answer += "R"
            cur_right = grid[num]
        else:
            y, x = grid[num]
            left_dis = get_dis(y, x, cur_left[0], cur_left[1])
            right_dis = get_dis(y, x, cur_right[0], cur_right[1])
            if left_dis < right_dis:
                answer += "L"
                cur_left = grid[num]
            elif left_dis > right_dis:
                answer += "R"
                cur_right = grid[num]
            else:
                if hand == "left":
                    answer += "L"
                    cur_left = grid[num]
                else:
                    answer += "R"
                    cur_right = grid[num]
    
    return answer