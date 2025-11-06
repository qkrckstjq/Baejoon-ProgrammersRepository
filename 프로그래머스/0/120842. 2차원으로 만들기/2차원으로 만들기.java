import java.util.*;
import java.util.stream.*;

class Solution {
    public int[][] solution(int[] num_list, int n) {
        return IntStream.range(0, num_list.length / n)
                .mapToObj(i -> Arrays.copyOfRange(num_list, i * n, i * n + n))
                .toArray(int[][]::new);
    }
}
