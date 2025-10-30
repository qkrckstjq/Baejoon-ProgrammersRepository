import java.util.*;
class Solution {
    public int solution(int n) {
        int num = 1;
        for(int i = 0; i <= 10; i++) {
            num *= (i == 0 ? 1 : i);
            if(n < num) return i - 1;
        }
        return 10;
    }
}