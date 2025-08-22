import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> result = new ArrayList<>();
        for(int[] command : commands) {
            int i = command[0] - 1;
            int j = command[1];
            int k = command[2] - 1;
            List<Integer> temp = new ArrayList<>();
            for(int q = i; q < j; q++) {
                temp.add(array[q]);
            }
            Collections.sort(temp);
            result.add(temp.get(k));
        }
        int[] answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}