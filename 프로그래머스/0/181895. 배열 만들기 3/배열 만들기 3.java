import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < intervals.length; i++) {
            int[] se = intervals[i];
            for(int j = se[0]; j <= se[1]; j++) {
                result.add(arr[j]);
            }
        }
        int[] answer = new int[result.size()];
        for(int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}