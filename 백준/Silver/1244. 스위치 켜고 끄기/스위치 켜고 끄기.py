import sys

def s_input():
    return sys.stdin.readline().strip()

def switching(number, switch):
    if switch[number] == 1:
        switch[number] = 0
    else:
        switch[number] = 1

def male(number, switch):
    switch_len = len(switch)
    for i in range(number - 1, switch_len, number):
        switching(i, switch)

def female(number, switch):
    switching(number - 1, switch)
    switch_len = len(switch)
    left = number - 2
    right = number
    while 0 <= left and right < switch_len:
        if switch[left] == switch[right]:
            switching(left, switch)
            switching(right, switch)
        else:
            return
        left -= 1
        right += 1



switch_len = int(s_input())
switch = list(map(int, s_input().split(" ")))
people = int(s_input())
for _ in range(people):
    gender, number = list(map(int, s_input().split(" ")))
    if gender == 1:
        male(number, switch)
    elif gender == 2:
        female(number, switch)

result = ""
for i in range(switch_len):
    result += str(switch[i]) + ' '
    if (i + 1) % 20 == 0:
        result += '\n'

print(result)