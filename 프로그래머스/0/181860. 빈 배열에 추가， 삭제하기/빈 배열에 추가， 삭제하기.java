import java.util.*;
class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            int num = arr[i];
            if(flag[i]) {
                for(int j = 0; j < num * 2; j++) {
                    answer.add(num);
                }
            } else {
                for(int j = 0; j < num; j++) {
                    answer.remove(answer.size() - 1);
                }
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}