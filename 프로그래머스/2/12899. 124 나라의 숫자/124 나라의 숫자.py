def solution(n):
    answer = ""

    while n > 0:
        n, r = divmod(n, 3)

        if r == 0:
            answer = "4" + answer
            n -= 1
        elif r == 1:
            answer = "1" + answer
        else:
            answer = "2" + answer

    return answer