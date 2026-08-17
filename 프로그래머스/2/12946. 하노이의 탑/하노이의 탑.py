def solution(n):
    answer = []

    def hanoi(count, start, end, via):
        if count == 1:
            answer.append([start, end])
            return

        hanoi(count - 1, start, via, end)
        answer.append([start, end])
        hanoi(count - 1, via, end, start)

    hanoi(n, 1, 3, 2)

    return answer