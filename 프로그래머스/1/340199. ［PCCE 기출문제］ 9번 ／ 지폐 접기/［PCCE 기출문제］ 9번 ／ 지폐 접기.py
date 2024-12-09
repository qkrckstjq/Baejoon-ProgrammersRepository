def solution(wallet, bill):
    def check_insert(wallet, bill):
        no_rotate = wallet[0] >= bill[0] and wallet[1] >= bill[1]
        rotate = wallet[0] >= bill[1] and wallet[1] >= bill[0]
        if no_rotate or rotate:
            return True
        return False
    answer = 0
    while True:
        if check_insert(wallet, bill):
            break
        if bill[0] < bill[1]:
            bill[1] = int(bill[1] / 2)
        else:
            bill[0] = int(bill[0] / 2)
        answer += 1
    return answer