class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int commonD = gcd(denom1, denom2);
        
        int answerD = denom1 * denom2 / commonD;
        int answerN = (answerD / denom1 * numer1) + (answerD / denom2 * numer2);
        
        int d = gcd(answerD, answerN);
        
        answer[0] = answerN / d;
        answer[1] = answerD / d;
        
        return answer;
    }
    
    public static int gcd(int num1, int num2) {
        int a = Math.max(num1, num2);
        int b = Math.min(num1, num2);
        
        int temp = 0;
        while(b != 0){
            temp = a;
            a = b;
            b = temp % b;
        }
        
        return a;
    }
}