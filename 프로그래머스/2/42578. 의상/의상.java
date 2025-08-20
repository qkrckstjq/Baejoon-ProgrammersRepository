import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> hash = new HashMap<>();
        for(String[] info : clothes) {
            String name = info[0];
            String type = info[1];
            
            hash.put(type, hash.getOrDefault(type, 0) + 1);
        }
        
        for(Integer i : hash.values()) {
            answer *= (i + 1);
        }
        
        return answer - 1;
    }
}