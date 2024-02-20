import sys


def s_input():
    return sys.stdin.readline().strip()


N = int(s_input())
city = list(map(int, s_input().split(" ")))
total = sum(city)
price = list(map(int, s_input().split(" ")))
result = 0
for i in range(len(price)):
    price[i] = (price[i], i)
price.sort(key=lambda x:x[0])
start = 0
end = len(price) - 1

for i in range(len(price)):
    if start <= price[i][1] <= end:
        temp = sum(city[price[i][1]:end])
        end = price[i][1]
        result += temp * price[i][0]
        total -= temp
        if total == 0:
            break
print(result)