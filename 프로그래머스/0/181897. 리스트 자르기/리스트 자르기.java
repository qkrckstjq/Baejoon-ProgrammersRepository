import java.util.*;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        List<Integer> result = new ArrayList<>();
        int start = 0;
        int end = 0;
        int term = 0;
        
        if(n == 1) {
            end = slicer[1];
        } else if(n == 2) {
            start = slicer[0];
            end = num_list.length - 1;
        } else if(n == 3) {
            start = slicer[0];
            end = slicer[1];
        } else {
            start = slicer[0];
            end = slicer[1];
            term = slicer[2] - 1;
        }
            
        for(int i = start; i <= end; i++) {
            result.add(num_list[i]);
            i += term;

        }
        int[] answer = new int[result.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = result.get(i);
        }
        return answer;
    }
}