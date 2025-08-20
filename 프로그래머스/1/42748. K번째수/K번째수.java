import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++) {
            int s = commands[i][0];
            int e = commands[i][1];
            int k = commands[i][2];
            List<Integer> temp = new ArrayList<>();
            for(int q = s - 1; q < e; q++) {
                temp.add(array[q]);
            }
            Collections.sort(temp);
            answer[i] = temp.get(k - 1);
        }
        
        
        
        return answer;
    }
}