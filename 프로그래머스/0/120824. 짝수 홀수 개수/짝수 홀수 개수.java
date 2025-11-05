import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        return Arrays.stream(num_list)
            .boxed()
            .reduce(new int[]{0, 0}, (answer, num) -> {
                answer[num % 2 == 0 ? 0 : 1]++;
                return answer;                    
            }, (a, b) -> new int[]{a[0] + b[0], a[1] + b[1]});
    }
}