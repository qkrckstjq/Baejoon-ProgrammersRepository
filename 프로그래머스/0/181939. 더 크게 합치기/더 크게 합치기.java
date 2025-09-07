import java.util.*;

class Solution {
    public int solution(int a, int b) {
        int answer = Math.max(Integer.parseInt(Integer.toString(a) + Integer.toString(b)), Integer.parseInt(Integer.toString(b) + Integer.toString(a)));
        
        return answer;
    }
}