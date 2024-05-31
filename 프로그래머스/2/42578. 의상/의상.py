memo = {}

def factorial(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial(n - 1)
    return memo[n]

def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

def solution(clothes):
    cloth = {}
    answer = 1
    
    for name, cloth_type in clothes:
        if cloth_type in cloth:
            cloth[cloth_type] += 1
        else:
            cloth[cloth_type] = 1
            
    for key in cloth:
        answer *= (cloth[key] + 1)
        
    return answer - 1

