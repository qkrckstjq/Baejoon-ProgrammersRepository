def solution(data, col, row_begin, row_end):
    data.sort(key=lambda row: (row[col - 1], -row[0]))

    answer = 0

    for i in range(row_begin, row_end + 1):
        s = 0
        for value in data[i - 1]:
            s += value % i
        answer ^= s

    return answer