import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);
        return IntStream.range(0, 5).map(i -> num_list[i]).toArray();
    }
}