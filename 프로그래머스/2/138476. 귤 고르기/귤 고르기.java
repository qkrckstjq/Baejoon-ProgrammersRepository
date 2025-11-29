import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int c : tangerine) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        List<Integer> counts = new ArrayList<>();
        for(int count : map.values()) {
            counts.add(count);
        }
        
        counts.sort(Comparator.comparing(i -> i));
        int temp = 0;
        int answer = 0;
        for(int i = counts.size() - 1; i >= 0; i--) {
            temp += counts.get(i);
            answer += 1;
            if(temp >= k) return answer;
        }
        return answer;
    }
}