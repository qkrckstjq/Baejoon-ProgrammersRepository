import java.util.*;


class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> comp = new HashMap<>();
        for(String c : participant) comp.put(c, comp.getOrDefault(c, 0) + 1);
        
        for(String p : completion) {
            int r = comp.get(p);
            if(r - 1 == 0) {
                comp.remove(p);
                continue;
            }
            comp.put(p, r - 1);
        }
        String answer = "";
        for(String a : comp.keySet()) {
            return answer = a;
        }
        return answer;
    }
}