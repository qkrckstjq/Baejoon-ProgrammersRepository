while True:
    num = input()
    if num == "0":
        break
    num = list(num)
    if len(num) % 2 == 0: #짝수일 경ㅇ
        i = (len(num) // 2) - 1
        j = len(num) // 2
    else:
        i = len(num) // 2 - 1
        j = len(num) // 2 + 1
    
    find = True
    for _ in range(len(num) // 2):
        if num[i] != num[j]:
            print("no")
            find = False
            break
        i -= 1
        j += 1
    if find:
        print("yes")