import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
city = list(map(int, s_input().split(" ")))
total = sum(city)
price = list(map(int, s_input().split(" ")))
price.sort()
result = 0
for i in range(len(price)):
    price[i] = (price[i], i)
    
for i in range(len(price)):
    if price[i][1] < len(city) - 1:
        temp = sum(city[price[i][1]:])
        result = temp * price[i][0]
        total -= temp
        if total == 0:
            break
print(result)
    
