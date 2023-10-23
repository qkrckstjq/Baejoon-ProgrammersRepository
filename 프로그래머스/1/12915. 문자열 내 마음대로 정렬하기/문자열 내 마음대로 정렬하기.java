import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, new Comparator<String> () {
            @Override
            public int compare (String a, String b) {
                int aValue = (int) a.charAt(n);
                int bValue = (int) b.charAt(n); 
                if(aValue == bValue) {
                    return a.compareTo(b);
                } else {
                    return aValue - bValue;
                }
                
            }
        });
        return strings;
    }
}
