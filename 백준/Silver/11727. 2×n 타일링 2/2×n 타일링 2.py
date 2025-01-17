N = int(input())
arr = [0, 1, 3, 5, 11]

def sim_fibo(num):
    if len(arr) > num:
        return arr[num]
    last = arr[-1]
    second = arr[len(arr) - 2] * 2
    arr.append(last + second)
    return sim_fibo(num)

print(sim_fibo(N)%10007)