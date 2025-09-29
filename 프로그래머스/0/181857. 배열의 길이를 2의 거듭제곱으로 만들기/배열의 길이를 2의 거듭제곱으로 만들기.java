import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = Arrays.stream(arr).boxed().collect(Collectors.toList());
        int q = 1;
        while(q < answer.size()) {
            q *= 2;
        }
        while(q > answer.size()) {
            answer.add(0);
        }
        return answer.stream().mapToInt(s -> s).toArray();
    }
}