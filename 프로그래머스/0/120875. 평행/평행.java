import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        double case1 = deg(dots[0], dots[1]);
        double case2 = deg(dots[2], dots[3]);
        
        double case3 = deg(dots[0], dots[2]);
        double case4 = deg(dots[1], dots[3]);
        
        double case5 = deg(dots[0], dots[3]);
        double case6 = deg(dots[1], dots[2]);
        
        if(case1 == case2 || case3 == case4 || case5 == case6) return 1;
        return 0;
    }
    
    public double deg(int[] a, int[] b) {
        return (double)(b[1] - a[1]) / (double)(b[0] - a[0]);
    }
}