from collections import deque

def press(arr, size):
    dq = deque()
    result = []

    for i in range(len(arr)):
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        dq.append(i)

        while dq and dq[0] <= i - size:
            dq.popleft()

        if i >= size - 1:
            result.append(arr[dq[0]])

    return result

def solution(m, n, h, w, drops):
    answer = []
    board = [[123456789] * n for _ in range(m)]
    for i, (y, x) in enumerate(drops):
        board[y][x] = i
    
    row_press = [press(board[i], w) for i in range(m)]
    total_press = [press([row_press[j][i] for j in range(len(row_press))], h) for i in range(len(row_press[0]))]
    
    result = -1
    for i in range(len(total_press[0])):
        for j in range(len(total_press)):
            if(total_press[j][i] > result):
                answer = [i, j]
                result = total_press[j][i]
                
    return answer
    