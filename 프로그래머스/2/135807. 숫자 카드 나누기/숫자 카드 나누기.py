from math import gcd

def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()
    
    numA = arrayA[0]
    for num in arrayA[1:]:
        numA = gcd(numA, num)
        
    numB = arrayB[0]
    for num in arrayB[1:]:
        numB = gcd(numB, num)

    
    if numB != 1:
        for num in arrayA:
            if num < numB:
                continue
            if num % numB == 0:
                numB = 1
                break;
    
    if numA != 1:
        for num in arrayB:
            if num < numA:
                continue
            if num % numA == 0:
                numA = 1
                break;
    
    print(numA, numB)
    
    answer = max(numA, numB)
    if answer == 1:
        answer = 0
    return answer
