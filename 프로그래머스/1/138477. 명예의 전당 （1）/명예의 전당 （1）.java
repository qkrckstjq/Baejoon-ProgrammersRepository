import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        ArrayList<Integer> temp = new ArrayList<Integer>(k);
        
        for(int i = 0; i < score.length; i++) {
            temp.add(score[i]);
            Collections.sort(temp);
            if(temp.size() > k) {
                temp.remove(0);
            }
            answer[i] = temp.get(0);
        }
        return answer;
    }
}