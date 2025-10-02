import java.util.stream.*;
class Solution {
    public int[][] solution(int n) {
        return IntStream.range(0, n)
            .mapToObj(i -> {
                int[] arr = new int[n];
                arr[i] = 1;
                return arr;
            }).toArray(int[][]::new);
    }
}