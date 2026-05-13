import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> comb = new HashMap<>();
        for(String[] c : clothes) {
            String type = c[1];
            comb.put(type, comb.getOrDefault(type, 0) + 1);
        }
        int answer = 1;
        for(int k : comb.values()) {
            answer *= (k + 1);
        }
        
        
        return answer - 1;
    }
}