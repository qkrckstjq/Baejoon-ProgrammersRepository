def solution(w,h):
    return (w * h) - ((w + h) - gcd(w, h))

def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    
    while a % b != 0:
        temp = b
        b = a % b
        a = temp
    return b