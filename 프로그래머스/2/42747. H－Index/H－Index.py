def solution(citations):
    sorted_c = sorted(citations, reverse=True)
    h_index = 0
    for i, c in enumerate(sorted_c):
        if i + 1 <= c:
            h_index = i + 1
        else:
            break
    return h_index
