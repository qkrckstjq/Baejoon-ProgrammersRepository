def st():
    temp = 0
    turn = 0

    papers, want = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers[want], temp = temp, numbers[want]
    while(numbers[0]!=0 or temp<max(numbers)):
        #print(numbers)
        max_c = max(numbers)
        popped = numbers.pop(0)
        if max_c!=popped or max_c<temp:
            numbers.append(popped)
        else:
            turn +=1
            #print(turn)
    turn+=1
    return turn


num = int(input())

for i in range(num):
    print(st())