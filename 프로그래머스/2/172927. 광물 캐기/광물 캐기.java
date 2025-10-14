import java.util.*;
class Solution {
    public int answer = Integer.MAX_VALUE;
    public int solution(int[] picks, String[] minerals) {
        back(picks, minerals, 0, 0);
        return answer;
    }
    
    public void back(int[] picks, String[] minerals, int m, int curA) {
        if(m >= minerals.length || Arrays.stream(picks).sum() == 0) {
            answer = Math.min(answer, curA);
            return;
        }
        if(curA >= answer) return;
        
        for(int i = 0; i < 3; i++){
            if(picks[i] > 0) {
                picks[i]--;
                int tempA = curA;
                for(int j = m; j < Math.min(m + 5, minerals.length); j++) {
                    tempA += getD(i, minerals[j]);
                }
                back(picks, minerals, Math.min(m + 5, minerals.length), tempA);
                picks[i]++;
            }   
        }
    }
    
    public int getD(int i, String type) {
        if (type.equals("diamond")) {
            int[] t = {1, 5, 25};
            return t[i];
        } else if (type.equals("iron")) {
            int[] t = {1, 1, 5};
            return t[i];
        } else { // stone
            return 1; // {1,1,1}[i]
        }
    }
}