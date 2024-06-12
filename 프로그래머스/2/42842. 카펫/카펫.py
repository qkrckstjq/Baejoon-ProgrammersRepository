def solution(brown, yellow):
    area = brown + yellow
    min_height = int(yellow ** 0.5)
    min_width = 1
    while True:
        if yellow % min_width == 0:
            min_height = yellow // min_width
            if (min_width + 2) * (min_height + 2) == area:
                break
        min_width += 1
        
    answer = [min_height + 2, min_width + 2]
    return answer