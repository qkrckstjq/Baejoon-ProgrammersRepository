import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        Set<Integer> originalLost = new HashSet<>();
        Set<Integer> originalReserve = new HashSet<>();
        
        for(int l : lost) originalLost.add(l);
        for(int r : reserve) originalReserve.add(r);
        
        List<Integer> dup = new ArrayList<>();
        
        for(Integer l : originalLost) if(originalReserve.contains(l)) dup.add(l);
        
        for(Integer d : dup) {
            originalLost.remove(d);
            originalReserve.remove(d);
        }
        
        for(Integer l : originalLost) {
            if(originalReserve.contains(l - 1)) {
                answer += 1;
                originalReserve.remove(l - 1);
            } else if(originalReserve.contains(l + 1)) {
                answer += 1;
                originalReserve.remove(l + 1);
            }
        }
        
        return n - (lost.length - dup.size() - answer);
    }
}