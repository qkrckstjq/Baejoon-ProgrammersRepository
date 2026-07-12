import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Map<Integer, Integer> left = new HashMap<>();
        Map<Integer, Integer> right = new HashMap<>();
        
        for(int t : topping) {
            right.put(t, right.getOrDefault(t, 0) + 1);
        }
        
        for(int t : topping) {
            left.put(t, left.getOrDefault(t, 0) + 1);
            right.put(t, right.get(t) - 1);
            if(right.get(t) == 0) {
                right.remove(t);
            }
            
            if(left.keySet().size() == right.keySet().size()) answer++;
        }
        
        return answer;
    }
}