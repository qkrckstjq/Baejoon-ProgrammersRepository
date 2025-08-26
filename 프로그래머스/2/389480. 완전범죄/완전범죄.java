import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        long totalB = 0;
        for (int[] x : info) totalB += x[1];

        if (totalB < m) return 0;

        long T = totalB - (m - 1);  
        if (T <= 0) return 0;

        int cap = n - 1;            
        if (cap <= 0) return -1;    

        long NEG = Long.MIN_VALUE / 4;
        long[] dp = new long[cap + 1];
        Arrays.fill(dp, NEG);
        dp[0] = 0;

        for (int[] it : info) {
            int a = it[0], b = it[1];
            if (a > cap) continue; 
            for (int s = cap; s >= a; --s) {
                if (dp[s - a] != NEG) {
                    dp[s] = Math.max(dp[s], dp[s - a] + b);
                }
            }
        }
        for (int a = 0; a <= cap; ++a) {
            if (dp[a] >= T) return a;
        }
        return -1;
    }
}