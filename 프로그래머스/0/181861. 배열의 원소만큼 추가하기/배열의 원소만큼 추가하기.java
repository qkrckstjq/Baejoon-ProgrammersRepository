import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            int num = arr[i];
            for(int j = 0; j < num; j++) {
                answer.add(num);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}