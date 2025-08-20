import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> hash = new HashMap<>();
        for (String p : participant) {
            hash.put(p, hash.getOrDefault(p, 0) + 1);
        }
        
        for (String c : completion) {
            Integer num = hash.get(c);
            if(num != null) {
                hash.put(c, num - 1);
                if(num - 1 == 0) {
                    hash.remove(c);
                }
            }
            
            
        }
        
        String answer = "";
        for(String l : hash.keySet()) {
            answer = l;
        }
        
        return answer;
    }
}