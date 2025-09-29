import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        List<Integer> ans = new ArrayList<>(k);
        Set<Integer> seen = new HashSet<>();
        
        for (int x : arr) {
            if (seen.add(x)) {    
                ans.add(x);
                if (ans.size() == k) break;
            }
        }
        while (ans.size() < k) ans.add(-1);
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
