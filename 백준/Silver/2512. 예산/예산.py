import sys

def s_input():
    return sys.stdin.readline().strip()

N = int(s_input())
moneys = list(map(int, s_input().split(" ")))
total_money = int(s_input())
moneys.sort()
result = 0
for i in range(len(moneys)):
    max_money = total_money // (N - i)
    if max_money >= moneys[i]:
        total_money -= moneys[i]
        result = moneys[i]
    else:
        result = max_money
        break
print(result)