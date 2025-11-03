class Solution {
    public int solution(int n) {
        return (n * 6) / gcd(n, 6) / 6;
    }
    
    public int gcd(int a, int b) {
        int tmp, n;
        
        if (a < b) {
            tmp = a;
            a = b;
            b = tmp;
        }
        
        while (b != 0) {
            n = a % b;
            a = b;
            b = n;
        }
        return a;
    }
}