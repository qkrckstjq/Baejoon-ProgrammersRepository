def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numbers = list(map(int, input().split(" ")))
result = float('inf')
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        i_j = (numbers[i] * numbers[j]) // gcd(numbers[i], numbers[j])
        for k in range(j + 1, len(numbers)):
            i_j_k = (i_j * numbers[k]) // gcd(i_j, numbers[k])
            result = min(i_j_k, result)

print(result)