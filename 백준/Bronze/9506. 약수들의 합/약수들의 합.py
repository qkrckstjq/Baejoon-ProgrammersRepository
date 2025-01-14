while True:
    num = int(input())
    if num == -1:
        break
    result = []
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
    if sum(result) == num:
        string = " + ".join(list(map(str, result)))
        print(f"{num} = {string}")
    else:
        print(f"{num} is NOT perfect.")