def solution(number, limit, power):
    
    def get_prime(num):
        result = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                result += 1 if i * i == num else 2
            if result > limit:
                return power
        return result
    
    answer = 0
    for i in range(1, number + 1):
        answer += get_prime(i)
    return answer