import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> hash = new HashMap<>();
        for(String p : participant) {
            hash.put(p, hash.getOrDefault(p, 0) + 1);
        }
        
        for(String c : completion) {
            hash.put(c, hash.get(c) - 1);
            if(hash.get(c) == 0) {
                hash.remove(c);
            }
        }
        
        for(String p : hash.keySet()) {
            answer = p;   
        }
        
        return answer;
    }
}