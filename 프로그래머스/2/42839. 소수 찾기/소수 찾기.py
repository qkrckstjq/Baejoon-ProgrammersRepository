from itertools import permutations

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    splited_nums = list(numbers)
    dup = set()
    for i in range(1, len(splited_nums) + 1):
        for list_nums in list(permutations(splited_nums, i)):
            join = int(''.join(list_nums))
            if not join in dup and check_prime(join):
                dup.add(join)
                answer += 1
    return answer