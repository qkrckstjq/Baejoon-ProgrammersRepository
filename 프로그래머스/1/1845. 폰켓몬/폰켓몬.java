import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        for(Integer i : nums) {
            set.add(i);
        }
        Integer removed = set.size();
        Integer half = nums.length / 2;
        return removed > half ? half : removed; 
        
    }
}