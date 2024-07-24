import sys;

possible = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}

def find_two(dice):
    min_two = 10000000000
    for i in range(len(dice)):
        for j in range(len(dice)):
            if i == j:
                continue
            if possible[i] == j or possible[j] == i:
                continue
            min_two = min(dice[i] + dice[j], min_two)
    return min_two

def find_three(dice):
    min_three = 100000000000
    for i in range(len(dice)):
        for j in range(len(dice)):
            if i == j:
                continue
            for k in range(len(dice)):
                if i == k or j == k:
                    continue
                if possible[i] == j or possible[i] == k or possible[j] == i or possible[j] == k or possible[k] == i or possible[k] == j:
                    continue
                min_three = min(dice[i] + dice[j] + dice[k], min_three)
    return min_three
                
                

N = int(input())
graph = {}
dice = list(map(int, (input().split(" "))))

if N == 1:
    print(sum(dice) - max(dice))
else:
    one = min(dice)
    two = find_two(dice)
    three = find_three(dice)
    
    sum_one = ((N - 2) * (N - 1) * one * 4) + (N - 2) ** 2 * one
    sum_two = ((N - 1) * two * 4) + ((N - 2) * two * 4)
    sum_three = three * 4
    
    print(sum_one + sum_two + sum_three)