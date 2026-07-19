def solution(m, n, startX, startY, balls):
    answer = []

    for ballX, ballY in balls:
        min_dist = float("inf")


        if not (ballX == startX and ballY > startY):
            dx = startX - ballX
            dy = startY - (2 * n - ballY)
            min_dist = min(min_dist, dx * dx + dy * dy)


        if not (ballX == startX and ballY < startY):
            dx = startX - ballX
            dy = startY + ballY
            min_dist = min(min_dist, dx * dx + dy * dy)


        if not (ballY == startY and ballX < startX):
            dx = startX + ballX
            dy = startY - ballY
            min_dist = min(min_dist, dx * dx + dy * dy)

      
        if not (ballY == startY and ballX > startX):
            dx = startX - (2 * m - ballX)
            dy = startY - ballY
            min_dist = min(min_dist, dx * dx + dy * dy)

        answer.append(min_dist)

    return answer