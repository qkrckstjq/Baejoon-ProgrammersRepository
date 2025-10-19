import java.util.*;
class Solution {
    public int solution(String before, String after) {
        String[] b = before.split("");
        String[] a = after.split("");
        Arrays.sort(b);
        Arrays.sort(a);
        if(b.length != a.length) {
            return 0;
        }
        for(int i = 0; i < b.length; i++) {
            if(!b[i].equals(a[i])) return 0;
        }
        return 1;
    }
}